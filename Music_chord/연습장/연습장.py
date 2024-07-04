from pdf_chord_extraction_functionalization import text_setting, text_chords, Find_chords
from roman import harmonics
from music_pattern import texting,find_repeated_segments,export_to_csv
from line_filter import line_filter
import pandas as pd
import re,os
from PyPDF2 import PdfReader
#%% 곡분석
if __name__ == "__main__":
    folder_path = "C:/Python/Syntex/working/개인/악보" # 악보 폴더 위치
    title = input("곡 제목을 말해주세요 :")
    file_path = os.path.join(folder_path, f"{title}.pdf")
    lines,key_name,title = text_setting(file_path)
    cleaned_lines = text_chords(lines)
    
Key_name = pd.read_csv("Key_signature.csv", index_col='KEY') # 다시 키 기준으로 &b을 찾는다


pattern = '|'.join(re.escape(sig) for sig in Key_name["Key_signature"]) # 패턴만들어서 
pattern = pattern.replace(r'\&b', r'\&b+') 

filtered = []
for text_line in cleaned_lines:
    matches = re.findall(pattern,text_line)
    filtered.append(matches)              # 패턴의 맞는 텍스트만 남김
    
# 키가 바뀔때마다 바뀌는 행을 구함
change_indices = []
last_value = None
for i, current_value in enumerate(filtered):
    if current_value not in ([], last_value):
        change_indices.append(i)
        last_value = current_value

Key_Trans = []
for i in range(len(change_indices)):
    x = change_indices[i]
    Trans = filtered[x]
    Key_Trans.append(Trans)

# &bb상태에서 다시 ?_key로 바꾸는 과정
Order_of_keys = []
Frame_values = Key_name.values
for information in Key_Trans:
    if information in Frame_values:
        key_name = Key_name.loc[Frame_values == information].index[0]
        Order_of_keys.append(key_name) 
        
# 끝을 설정해주고
text_separation = {}
change_indices.append(len(cleaned_lines))
# cleaned_lines에서 조표에 맞춰서 분리
for i in range(len(change_indices) - 1):
    start_idx = change_indices[i]
    end_idx = change_indices[i + 1]
    text_separation[i] = cleaned_lines[start_idx:end_idx]


#%%%

title = os.path.basename(file_path)
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

try:
    Key_name = pd.read_csv("Key_signature.csv", index_col='KEY')
except:
    print("Key_name의 정보가 없습니다.다시 설정해주세요.")

pattern = '|'.join(re.escape(sig) for sig in Key_name["Key_signature"])
pattern = pattern.replace(r'\&b', r'\&b+') 
extracted_parts = []

for line in filtered_lines:
    cleaned_line = line.replace(" ", "") # 빈칸 삭제
    matches = re.findall(pattern,cleaned_line)
    if matches:
        extracted_parts.extend(matches)

print(extracted_parts)
seen = set()
unique_parts = [x for x in extracted_parts if x not in seen and not seen.add(x)]
Frame_values = Key_name.values

parts_with_keys = []
for part in unique_parts:
    if part in Frame_values:
        key_name = Key_name.loc[Frame_values == part].index[0]
        parts_with_keys.append(key_name)

