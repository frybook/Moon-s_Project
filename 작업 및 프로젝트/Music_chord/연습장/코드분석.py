import pandas as pd
#%%
# key가 인덱스로 values는 
KEY = ['C_Key','F_Key','Bb_Key','Eb_Key','Ab_Key','Dd_Key','Gb_Key','B_Key','E_Key','A_Key','D_Key','G_Key']
# 문자 슬라이싱
harmony = "G7"
harmony = "Ⅴ" + harmony[1:]
print(harmony)


#%%
# pdf 곡 text화

from PyPDF2 import PdfReader

# reader = PdfReader("시든꽃의물을주듯.pdf")
# reader = PdfReader("예뻤어.pdf")
# reader = PdfReader("잘지내요.pdf") # 성공
# reader = PdfReader("휠릴리.pdf")
# reader = PdfReader("그때.pdf")
# reader = PdfReader("먹구름.pdf")

def text_setting():
    title = input("곡 제목을 말해주세요")
    reader = PdfReader(f"{title}.pdf")
    pages = reader.pages
    text = ""
    for page in pages:
        sub = page.extract_text()
        text += sub
    lines = text.split('\n')
    return lines


#%%
# 가사와 코드를 마디 기준으로 분리화
import re

# korean_pattern = re.compile(r'[\uac00-\ud7af]+') # 한국어 가사(영어가사 나올경우 안나옴 해결해야됌) 
# korean_text = []
# Split the text into lines
# lines = text.split('\n')
cleaned_lines = []
exclude = input("제외할 문장을 말해주세요 : ")
for line in lines:
    line = line.replace(exclude, "").strip()
    line = line.replace("Feat", "").strip()
    cleaned_line = ''.join(line.split())
    cleaned_lines.append(cleaned_line)

#%%



# Process each line
# for line in lines:
    
#     # Find all Korean characters
#     korean_matches = korean_pattern.findall(line)
#     if korean_matches:
#         korean_text.append(' '.join(korean_matches))
    
    # Find all codes
def Find_chords(text):   
    codes = []
    chord_pattern = re.compile(r'[A-G](?:#|b)?(?:m(?:6|7|11)?|M(?:6|7)?|dim7?|7(?:sus4)?|sus4|add9|6|9|aug(?:7)?|mM7)?(?:\([#b]?(?:[0-9]|1[0-3])\))?(?:/[A-G](?:#|b)?)?')
    '''
    ?:[A-G][#b]? = 코드에 # or b 붙는지
    ?:m7|M7|m|7|dim7|sus4|add9|6|9|aug|aug7   코드가 어떻게 되는지
    (?:/[A-G][#b] ?) 코드에 베이스가 붙는지        
    (?:\((?:#|b)(?:[0-9]|1[0-3])\) #또는 b가 붙는데 0~13까지 숫자가 붙는지 *텐션 여부*
    '''
    for line in cleaned_lines:
        
        line1 = line.replace('˙', '').replace('œ', '').replace('N.C','').replace('D.S','').replace('Coda','').replace('.','').replace('‰','')
        # lyrics = re.sub(r'\b[A-Z][a-z]{2}\w*\b', '', line1) # 영어 제외시키려고 함
        
        code_matches = chord_pattern.findall(line1)
        if code_matches:
            codes.append(' '.join(code_matches))
    
    return codes

Chords = Find_chords(cleaned_lines)

#%%
'''
문제점
영어가사가 나올 경우 대문자를 코드로 인식함
(해결) A-Z 대문자1개소문자 2 라는 수식어
영어문제를 해결했더니 sus4를 안찾는게 있음
(해결) 걸러지는 순서를 반대로해서 음악 기보 텍스트 및 미디 텍스트를 먼저 제외
영어가 조건식이랑 다른경우 JTBC가 BC가 조건식에 걸려서 노출됌
'''