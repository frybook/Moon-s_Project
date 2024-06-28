from PyPDF2 import PdfReader

reader = PdfReader("시든꽃에물을주듯.pdf")
# page = reader.pages[3]
pages = reader.pages[0]
parts = []


def visitor_body(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    if y > 582 and y < 587:
        parts.append(text)

A = pages.extract_text()
pages.extract_text(visitor_text=visitor_body)
text_body = "".join(parts)

print(text_body)




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