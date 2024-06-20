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

    return lines,parts_with_keys

#%%

def text_chords(lines):
    cleaned_lines = []
    eraser = ["Feat","CODE","JTBC"]
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
def Find_chords(cleaned_lines):   
    chords = []
    formatted_chords = [] # 9sus4
    chord_pattern = re.compile(r'[A-G](?:#|b)?(?:m(?:6|7|11)?|M(?:6|7)?|dim7?|7(?:sus4)?|sus4|add9|6|9|aug(?:7)?|mM7)?(?:\([#b]?(?:[0-9]|1[0-3])\))?(?:/[A-G](?:#|b)?)?')
    for line in cleaned_lines:
        line1 = line.replace('˙', '').replace('œ', '').replace('N.C','').replace('D.S','').replace('Coda','').replace('.','').replace('‰','')        
        chord_matches = chord_pattern.findall(line1)
        if chord_matches:
            chords.append(' '.join(chord_matches))
    
    for chord_pair in chords:
        formatted_chords.append(', '.join([f'"{chord}"' for chord in chord_pair.split()]))
    chords2 = []
    for chord_string in formatted_chords:
        pairs = chord_string.split(', ')
        chords2.append([pair.strip('"') for pair in pairs])
    
    return chords2


