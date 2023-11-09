import pdfplumber
import re
import os


INPUT_DIRECTORY_PATH = r"C:\Users\thheo\Documents\LLM_text_preprocessing\Removed_PDF"
OUTPUT_DIRECTORY_PATH = r"C:\Users\thheo\Documents\LLM_text_preprocessing\test"


# 출력 파일 생성
def create_output_file_path(input_file_path, output_directory_path):
    base_filename, file_extension = os.path.splitext(os.path.basename(input_file_path))
    new_filename = f"{base_filename}.txt"
    output_file_path = os.path.join(output_directory_path, new_filename)
    return output_file_path


# PDF->TEXT로 변환
def pdf_to_text_by_pdfplumber(input_file_path, output_file_path):
    
    # PDF 파일 열기
    with pdfplumber.open(input_file_path) as pdf: 
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            # PDF 페이지 마다 반복
            for page in pdf.pages:
                contents = page.extract_text()                      # PDF에서 텍스트 추출
                # contents = re.sub(r'\n', '', contents)            # newline 제거
                contents = re.sub(r'[\x00-\x1F\x7F]', '', contents) # ASCII 제어문자('FF','BEL','SUB' 등) 제거
                # print(contents)
                output_file.write(contents)
    


if __name__ == '__main__':
    file_list = os.listdir(INPUT_DIRECTORY_PATH)
    
    # PDF 약관 파일이 있는 폴더 순회
    for file_name in file_list:
        input_file_path = os.path.join(INPUT_DIRECTORY_PATH, file_name)
        output_file_path = create_output_file_path(input_file_path, OUTPUT_DIRECTORY_PATH)
        pdf_to_text_by_pdfplumber(input_file_path, output_file_path)






