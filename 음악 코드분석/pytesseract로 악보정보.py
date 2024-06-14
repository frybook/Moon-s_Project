from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import os

# PDF 파일 경로
pdf_file = "시든꽃의물을주듯.pdf"

# PDF를 이미지로 변환하여 임시 폴더에 저장
pages = convert_from_path(pdf_file, 600)  # 300 DPI로 변환

# 임시 이미지 파일들을 저장할 폴더 생성
temp_image_dir = 'temp_images'
os.makedirs(temp_image_dir, exist_ok=True)

image_texts = []

# 각 페이지에 대해 OCR 수행
for i, page in enumerate(pages):
    temp_image_path = os.path.join(temp_image_dir, f'page_{i+1}.png')
    page.save(temp_image_path, 'PNG')
    
    # 이미지에서 텍스트 추출
    text = pytesseract.image_to_string(Image.open(temp_image_path))
    image_texts.append(text)
    
    
#%%
# 임시 이미지 파일들 삭제
for file_path in os.listdir(temp_image_dir):
    os.remove(os.path.join(temp_image_dir, file_path))
os.rmdir(temp_image_dir)

# 추출된 텍스트 출력
for i, text in enumerate(image_texts):
    print(f'페이지 {i+1}:\n{text}\n')