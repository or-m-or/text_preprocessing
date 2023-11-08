import os
import datetime
import re



def extract_inputfile(input_directory_path, output_directory_path):
    
    #  '삼성생명', '삼성화재', '한화생명', '한화손해', 'KB손해'
    company_names = [
        '교보생명', '라이나생'
    ]


    file_list = os.listdir(input_directory_path)
    for file_name in file_list:
        file_path = os.path.join(input_directory_path, file_name)

        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as input_file:
                file_contents = input_file.read()

            company_name = file_name[:4]

            print(f"파일명: {file_name}, 보험사명: {company_name}")

            if company_name in company_names:
                output_contents = modified_contents(company_name, file_contents)
                create_output_path(company_name, file_path, output_directory_path, output_contents)
            else:
                print("company is not in company_names list")


"""
[교보생명]
- 그림, 표에 있는 문자열 처리는 어떻게?
- Form Feed 앞 newline 2개 같이 삭제함.
    1. form feed 삭제이후 띄어쓰기가 필요한 경우가 고려되지 않음 : ' ' 추가 필요
    2. 약관마다 표지 페이지 처리 필요

- 제거하지 말아야 할 newline
    1. '.'바로 뒤에 위치한 newline
    2. '제XX조', '제X조' 바로 앞에 위치한 newline
    3. '제X관' 바로 앞에 위치한 newline
    4. '제XX조', '제X조'+' (...)' 문자열 뒤에 위치한 newline
    5. '가.' 바로 앞에 위치한 newline

[라이나생명]

"""



def modified_contents(company_name, contents) -> str:

    # 페이지가 넘어갈 때마다 생기는 "FF(Form Feed), '\x0c'" 문자 제거
    contents_without_ff = re.sub(r'\n\n\x0c', '', contents)
    
    if company_name == '교보생명':
        # 필요 없는 newline 제거
        contents = re.sub(r'(\.)\n', r'\1####', contents_without_ff)
        contents = re.sub(r'\n(제\d조)', r'####\1', contents)
        contents = re.sub(r'\n(제\d관)', r'####\1', contents)
        contents = re.sub(r'(제\d+조 \(.*\))\n', r'\1####', contents)
        contents = re.sub(r'\n(가.)', r'####\1', contents)

        contents = contents.replace('\n', '')
        contents = contents.replace('####', '\n')    
        contents = re.sub(r'(제\d+조 \(.*\))', r'\n\1', contents)




    return contents



# 최종 출력결과 저장, output 파일 생성
def create_output_path(company_name, input_file_path, output_directory, modified_contents):
    if company_name != '교보생명':
        return "fail"
    current_date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base_filename, file_extension = os.path.splitext(os.path.basename(input_file_path))
    new_filename = f"{base_filename}_{current_date}{file_extension}"
    output_path = os.path.join(output_directory, new_filename)


    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(modified_contents)



if __name__ == "__main__":
    # 테스트 용, 임시 path, directory

    input_directory_path = r"C:\Users\thheo\Documents\LLM_text_preprocessing\Pretraining_TXT"
    output_directory_path = r"C:\Users\thheo\Documents\LLM_text_preprocessing\Pretraining_TXT_modify"
    

    extract_inputfile(input_directory_path, output_directory_path)
