import os
import datetime

def create_file(input_file_path, output_directory):
    current_date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base_filename, file_extension = os.path.splitext(os.path.basename(input_file_path))
    new_filename = f"{base_filename}_{current_date}{file_extension}"
    output_file_path = os.path.join(output_directory, new_filename)
    
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        pass




def delete_page_separator(content):
    # 페이지가 넘어갈 때마다 생기는 "FF" 문자 제거 - "\x0c"
    text_without_ff = [line.replace("\x0c", "") for line in input_lines]


if __name__ == "__main__":
    input_file_path = r"C:\Users\thheo\Documents\LLM_text_preprocessing\Pretraining_TXT\교보생명(무)교보LTC종신보험 중도부가특약_removed.txt"
    output_directory = r"C:\Users\thheo\Documents\LLM_text_preprocessing\Pretraining_TXT_modify"
    
    with open(input_file_path, "r", encoding="utf-8") as input_file:
        content = input_file.read()

    delete_page_separator(content)

    create_file(input_file_path, output_directory)





    