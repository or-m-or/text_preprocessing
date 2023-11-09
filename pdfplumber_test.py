import pdfplumber
import re

input_directory_path = r"C:\Users\thheo\Documents\LLM_text_preprocessing\Removed_PDF"
output_directory_path = r"C:\Users\thheo\Documents\LLM_text_preprocessing\Pretraining_TXT_modify"

FILE_PATH = r"C:\Users\thheo\Documents\LLM_text_preprocessing\Removed_PDF\한화손해개인용자동차보험(공동물건)_removed.pdf"
INDEX_OF_PAGE = 1


def text_to_txt_file(text, file_name):
    with open(file_name, "w") as f:
        f.write(text)


def pdf_to_text_by_pdfplumber():
    # PDF 파일 열기
    with pdfplumber.open(FILE_PATH) as pdf: 
        with open("all_pages_text.txt", "w", encoding="utf-8") as output_file:
            # PDF 페이지 마다 반복
            for page in pdf.pages:
                contents = page.extract_text()                      # PDF에서 텍스트 추출
                contents = re.sub(r'\n', '', contents)              # newline 제거
                contents = re.sub(r'[\x00-\x1F\x7F]', '', contents) # ASCII 제어문자('FF','BEL','SUB' 등) 제거
                output_file.write(contents) 

"""
def pdf_to_text_by_pdfplumber():
    with pdfplumber.open(FILE_PATH) as pdf:
        page = pdf.pages[INDEX_OF_PAGE]
        text = page.extract_text()
        text_to_txt_file(text, "text_by_pdfplumber.txt")
"""

if __name__ == '__main__':
    pdf_to_text_by_pdfplumber()
