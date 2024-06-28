from PyPDF2 import PdfReader
import pandas as pd
import re,os

#%%

def text_setting():
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
    
    pattern = '|'.join(re.escape(sig) for sig in Key_name["Key_signature"])
    pattern = pattern.replace(r'\&b', r'\&b+') 
    extracted_parts = []
    
    for line in lines:
        cleaned_line = line.replace(" ", "") # 빈칸 삭제
        matches = re.findall(pattern,cleaned_line)
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

    return lines,parts_with_keys,title
'''PDF를 텍스트로 변형하고 key 파악하기'''

#%% 
# 제거할 텍스트 영어를 제거해줘야된다.
def text_chords(lines):
    cleaned_lines = []
    eraser = ["Feat","CODE","JTBC","Fools",'DOKO',"YOUNHA","UNSTABLE MINDSET"]
    # print("대문자1 소문자 2개가 붙어있는 단어,문장을 제외해주세요")
    print("------------------------------------------------------")
    # exclude = input("제외할 문장을 말해주세요 : ")
    for line in lines:
        for trans in eraser:
            line = line.replace(trans, "")        
        cleaned_line = ''.join(line.split())
        cleaned_lines.append(cleaned_line)
    return cleaned_lines
#%%
# 딕셔너리로 
def Find_chords(text_separation):
    formatted_chords_dict = {}
    # chord_pattern = re.compile(r'[A-G](?:#|b)?(?:m(?:6|7|11|M7)?|M(?:6|7|9)?|dim7?|7(?:sus4)?|sus4|9sus4|add9|6|9|aug(?:7)?|mM7)?(?:\([#b]?(?:[0-9]|1[0-3])\))?(?:/[A-G](?:#|b)?)?')
    chord_pattern = re.compile(r'[A-G](?:#|b)?(?:m(?:6|7|11|M7)?|M(?:6|7|9)?|dim7?|7(?:sus4)?|sus4|9sus4|add9|6|9|aug(?:7)?|mM7|(?:add9))?(?:\([#b]?(?:[0-9]|1[0-3]|add9)\))?(?:/[A-G](?:#|b)?)?')

    for key, dict_lines in text_separation.items():
        chords = []
        for line in dict_lines:
            # 기본적으로 나오는 단어 정리
            line1 = line.replace('˙', '').replace('œ', '').replace('N.C', '').replace('D.S', '').replace('Coda', '').replace('.', '').replace('‰', '')        
            # 패턴으로 코드 찾기
            chord_matches = chord_pattern.findall(line1)
            if chord_matches:
                chords.append(' '.join(chord_matches))
        # 다시 딕셔너리로 모으는 작업
        formatted_chords_dict[key] = chords

    
    return formatted_chords_dict


