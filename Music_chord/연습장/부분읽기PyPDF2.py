from PyPDF2 import PdfReader
# 텍스트 읽는 파일
def process_pdf(file_path):
    reader = PdfReader(file_path)
    pages = reader.pages
    parts = []
    # 제목부분및 필요없는 부분 구간설정
    def visitor_body(text, cm, tm, fontDict, fontSize):
        y = tm[5]
        if y > 665:
            parts.append(text)

    # 페이지0번째 텍스트 제외구간 설정
    pages[0].extract_text(visitor_text=visitor_body)
    text_body_page_0 = "".join(parts)
    A = text_body_page_0.split('\n')

    # 전체 페이지 정보
    text = ""
    for page in pages:
        text += page.extract_text()

    lines = text.split('\n')

    # 전체에서 제외시킬 내용을 찾아 삭제
    filtered_lines = [line for line in lines if line not in A]

    return filtered_lines

# Example usage
file_path = "공감.pdf"
filtered_lines = process_pdf(file_path)

#%%


'''
#,b이 최소 5는 되야 나옴 79
y < 700 제목있는부분
y > 646 and y < 651
y > 565 and y < 570
y > 486 and y < 492
y > 408 and y < 413
y > 329 and y < 334
y > 250 and y < 255
y > 171 and y < 176
y > 93 and y < 98

86
y > 668 and y < 673
y > 582 and y < 587





'''

#%%%
from PyPDF2 import PdfReader

# PDF 파일 열기
reader = PdfReader("시든꽃에물을주듯.pdf")
pages = reader.pages[0]

# 제외할 좌표 영역 목록
exclude_areas = [
    (121, 708, 1798, 165),
    (121, 989, 1798, 151),
    (121, 1270, 1798, 151),
    (121, 1548, 1798, 158),
    (121, 1834, 1798, 146),
    (121, 2115, 1798, 156),
    (121, 2392, 1798, 151),
    (121, 2673, 1798, 150),
]

parts = []

def is_in_exclude_area(y):
    """주어진 y 좌표가 제외할 영역에 속하는지 확인"""
    for x, y_start, width, height in exclude_areas:
        y_end = y_start + height
        if y_start <= y <= y_end:
            return True
    return False

def visitor_body(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    if not is_in_exclude_area(y):
        parts.append(text)

# 페이지에서 텍스트 추출
pages.extract_text(visitor_text=visitor_body)
text_body = "".join(parts)

print(text_body)