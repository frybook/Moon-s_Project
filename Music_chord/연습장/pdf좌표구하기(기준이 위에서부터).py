import pdfplumber

def extract_text_with_coordinates(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            print(f"Page {i+1}")
            for word in page.extract_words():
                text = word['text']
                x0, y0, x1, y1 = word['x0'], word['top'], word['x1'], word['bottom']
                print(f"Text: {text}, Coordinates: ({x0}, {y0}, {x1}, {y1})")

# PDF 파일 경로 설정
pdf_path = "시든꽃에물을주듯.pdf"
A = extract_text_with_coordinates(pdf_path)