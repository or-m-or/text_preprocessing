import PyPDF2

def extract_text_without_footer(pdf_path, output_path):
    pdf = PyPDF2.PdfReader(open(pdf_path, 'rb'))
    with open(output_path, 'w', encoding='utf-8') as txt_file:
        for page_num in range(pdf.getNumPages()):
            page = pdf.getPage(page_num)
            
            # 페이지에서 텍스트 추출
            text = page.extractText()
            
            # 여기에서 필요한 텍스트 전처리를 수행합니다.
            
            # footer 및 side footer 제거
            # footer 또는 side footer가 텍스트에 포함된 특정 패턴을 찾아서 제거합니다.
            # text = text.replace("Footer Text", "")
            
            # form feed 제거 (페이지 나눔 문자)
            text = text.replace("\x0C", "")
            
            # 정제된 텍스트를 저장합니다.
            # txt_file.write(text)
            print(text)

input_ = r"C:\Users\thheo\Documents\LLM_text_preprocessing\Removed_PDF\교보생명(무)교보LTC종신보험 중도부가특약_removed.pdf"
output = r"C:\Users\thheo\Documents\LLM_text_preprocessing\Pretraining_TXT_modify"
extract_text_without_footer(input_, output)