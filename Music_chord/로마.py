import pandas as pd

# key가 인덱스로 values는 
KEY = ['C_Key','F_Key','Bb_Key','Eb_Key','Ab_Key','Dd_Key','Gb_Key','B_Key','E_Key','A_Key','D_Key','G_Key']
# 문자 슬라이싱

Chrods_name = {"Ⅰ" : ["C","F",  "Bb", "Eb", "Ab", "Db", "Gb","B", "E", "A", "D", "G"],
               "ⅱ" : ["D","G",  "C",  "F",  "Bb", "Eb", "Ab","C#","F#","B", "E", "A"],
               "ⅲ" : ["E","A",  "D",  "G",  "C",  "F",  "Bb","D#","G#","C#","F#","B"],
               "Ⅳ" : ["F","Bb", "Eb", "Ab", "Db", "Db", "B", "E", "A", "D", "G", "C"],
               "Ⅴ" : ["G","C",  "F",  "Bb", "Eb", "Ab", "Db","F#","B", "E" ,"A", "D"],
               "ⅵ" : ["A","D",  "G",  "C",  "F",  "Bb", "Eb","G#","C#","F#","B", "E"],
               "ⅶ" : ["B","E",  "A",  "D",  "G",  "C",  "F", "A#","D#","G#","C#","F#"]}


Frame = pd.DataFrame(Chrods_name,index = KEY)

#%%
harmony = "G7"
harmony = "Ⅴ" + harmony[1:]
print(harmony)
key = "Bb"
f'{key}_Key'
#%%
key = "Bb"  
# 찾고자 하는 코드 리스트
chord = ["BbM7", "F7", "Eb7", "BbM7/C", "E7"]

# 기본음을 추출하는 함수
def extract_base_note(note):
    if len(note) > 1 and note[1] in ['b', '#']:
        return note[:2]
    return note[0]

# 코드 타입을 추출하는 함수
def extract_chord_type(note):
    Characteristics_of_chord = {'m', 'M7', 'm7', '7',"sus4","7(b9)","m7(b5)","dim","7(#9)"} 
    if len(note) > 2 and note[2:] in Characteristics_of_chord:
        return note[2:]
    elif len(note) > 1 and note[1:] in Characteristics_of_chord:
        return note[1:]
    return ''

chord2 = []

for note in chord:
    base_note = extract_base_note(note)  # 코드의 기본음을 추출
    chord_type = extract_chord_type(note)  # 코드의 타입을 추출
    found = False
    
    for col_name in Frame.columns:
        if Frame.loc[f'{key}_Key', col_name] == base_note:
            if '/' in note:
                inversion_info = note.split('/')[1]  # 슬래시 다음 부분 추출
                chord2.append(f"{col_name}{chord_type}/{inversion_info}")
            else:
                chord2.append(f"{col_name}{chord_type}")
            found = True
            break  # 내부 루프 종료
    
    if not found:
        chord2.append(note)  # 기본음을 찾지 못한 경우 원래의 코드를 그대로 추가

print(chord2)
# note = "Eb7/C"
# base_note, inversion_info = note.split('/')
#%%
key = "Bb_Key"  # Use the exact index label that matches your DataFrame

# 찾고자 하는 코드 리스트
chord = ["Eb7/C","BbM7","Fm7"]

# 기본음을 추출하는 함수
def extract_base_note(note):
    if '/' in note:
        base_note = note.split('/')[0]  # 슬래시 이전 부분 추출
    else:
        base_note = note
    
    if len(base_note) > 1 and base_note[1] in ['b', '#']:
        return base_note[:2]
    return base_note[0]

# 코드 타입을 추출하는 함수
def extract_chord_type(note):
    Characteristics_of_chord = {'m', 'M7', 'm7', '7',"sus4","7(b9)","m7(b5)","dim","7(#9)"} 
    if len(note) > 2 and note[2:] in Characteristics_of_chord: # 길이가 2보타 크고 2이상부터 설정값을 가지고 있을경우
        return note[2:]
    elif len(note) > 1 and note[1:] in Characteristics_of_chord:
        return note[1:]
        
    return ''

chord2 = []

for note in chord:
    base_note = extract_base_note(note)  # 코드의 기본음을 추출
    chord_type = extract_chord_type(note)  # 코드의 타입을 추출
    found = False
    
    for col_name in Frame.columns:
        if Frame.loc[key, col_name] == base_note:
            roman_numeral = col_name  # Roman numeral corresponding to the base note
            if '/' in note:
                inversion_info = note.split('/')[1]  # 슬래시 다음 부분 추출
                chord2.append(f"{roman_numeral}{chord_type}/{inversion_info}")
            else:
                chord2.append(f"{roman_numeral}{chord_type}")
            found = True
            break  # 내부 루프 종료
    
    if not found:
        chord2.append(note)  # 기본음을 찾지 못한 경우 원래의 코드를 그대로 추가

print(chord2)
