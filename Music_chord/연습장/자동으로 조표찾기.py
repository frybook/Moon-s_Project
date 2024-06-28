from PyPDF2 import PdfReader
import pandas as pd
import re,os
# def text_setting():
try:    
    folder_path = "C:/Python/Syntex/working/개인/악보" # 악보 폴더 위치
    title = input("곡 제목을 말해주세요 :")
    file_path = os.path.join(folder_path, f"{title}.pdf")
except:
    print("현재 폴더에 악보가 없습니다. 다시 확인 해주세요.")
reader = PdfReader(file_path)
pages = reader.pages
text = ""
for page in pages:
    sub = page.extract_text()
    text += sub
lines = text.split('\n')

try:
    Key_name = pd.read_csv("Key_signature.csv", index_col='KEY')
except:
    print("Key_name의 정보가 없습니다.다시 설정해주세요.")

# pattern = '|'.join(Key_name["Key_signature"])
pattern = '|'.join(re.escape(sig) for sig in Key_name["Key_signature"])
pattern = pattern.replace(r'\&b', r'\&b+') 
extracted_parts = []

for line in lines:
    matches = re.findall(pattern, line)
    if matches:
        extracted_parts.extend(matches)

seen = set()
unique_parts = [x for x in extracted_parts if x not in seen and not seen.add(x)]
Frame_values = Key_name.values

parts_with_keys = []
for part in unique_parts:
    if part in Frame_values:
        key_name = Key_name.loc[Frame_values == part].index[0]
        parts_with_keys.append(key_name)

    # return lines,parts_with_keys
    
    
# key찾아서 나온 순서가 뒤죽박죽임 설정해야됌
# 이유: 전조의 순서에따라서 바뀌기 때문에 무조건 처음 그순서데로 지정해야될듯(수정)
# b키를 못읽음(수정)
