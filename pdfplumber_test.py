import pdfplumber

FILE_PATH = "220609(석간)_강남에서_자율주행_택시_달린다(첨단자동차과).pdf"
INDEX_OF_PAGE = 1


def text_to_txt_file(text, file_name):
    with open(file_name, "w") as f:
        f.write(text)


def pdf_to_text_by_pdfplumber():
    with pdfplumber.open(FILE_PATH) as pdf:
        page = pdf.pages[INDEX_OF_PAGE]
        text = page.extract_text()
        text_to_txt_file(text, "text_by_pdfplumber.txt")


if __name__ == '__main__':
    pdf_to_text_by_pdfplumber()
