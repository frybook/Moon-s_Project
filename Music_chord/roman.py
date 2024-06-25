import pandas as pd

KEY = ['C_Key','F_Key','Bb_Key','Eb_Key','Ab_Key','Db_Key','Gb_Key','B_Key','E_Key','A_Key','D_Key','G_Key']
Chrods_name = {"Ⅰ" : ["C","F",  "Bb", "Eb", "Ab", "Db", "Gb","B", "E", "A", "D", "G"],
               "ⅱ" : ["D","G",  "C",  "F",  "Bb", "Eb", "Ab","C#","F#","B", "E", "A"],
               "ⅲ" : ["E","A",  "D",  "G",  "C",  "F",  "Bb","D#","G#","C#","F#","B"],
               "Ⅳ" : ["F","Bb", "Eb", "Ab", "Db", "Gb", "B", "E", "A", "D", "G", "C"],
               "Ⅴ" : ["G","C",  "F",  "Bb", "Eb", "Ab", "Db","F#","B", "E" ,"A", "D"],
               "ⅵ" : ["A","D",  "G",  "C",  "F",  "Bb", "Eb","G#","C#","F#","B", "E"],
               "ⅶ" : ["B","E",  "A",  "D",  "G",  "C",  "F", "A#","D#","G#","C#","F#"]}
Frame = pd.DataFrame(Chrods_name,index = KEY)


# CSV파일로 저장하기
Frame.to_csv("Major_scale.csv", index_label='KEY')

# CSV파일 읽기
Major_scale = pd.read_csv("Major_scale.csv", index_col='KEY')
#%%
import pandas as pd
KEY = ['Am_Key','Dm_Key','Gm_Key','Cm_Key','Fm_Key','Bbm_Key','Ebm_Key','G#m_Key','C#m_Key','F#m_Key','Bm_Key','Em_Key']
Chrods_name = {"ⅰ" : ["A","D",  "G",  "C",   "F",  "Bb", "Eb", "G#", "C#", "F#", "Bm", "E"],
               "ⅱ" : ["B","E",  "A",  "D",   "G",  "C",  "F",  "A#", "D#", "G#", "C#", "F#"],
               "Ⅲ" : ["C","F",  "Bb", "Eb",  "Ab", "Db", "Gb", "B",  "E",  "A",  "D",  "G"],
               "ⅳ" : ["D","G",  "C",  "F",   "Bb", "Eb", "Ab", "C#", "F#", "B",  "E",  "A"],
               "Ⅴ" : ["E","A",  "D",  "G",   "C",  "F",  "Bb", "D#", "G#", "C#" ,"F#", "B"],
               "Ⅵ" : ["F","Bb", "Eb", "Ab",  "Db", "Gb", "B",  "E",  "A",  "D",  "G",  "C"],
               "Ⅶ" : ["G","C",  "F",  "Bb",  "Eb", "Ab", "Db", "F#", "B",  "E",  "A",  "D"]}
Frame2 = pd.DataFrame(Chrods_name,index = KEY)

Frame2.to_csv("minor_scale.csv", index_label='KEY')
minor_scale = pd.read_csv("minor_scale.csv", index_col='KEY')

#%%
# 플랫,샵으로 Key 찾기
KEY = ['C_Key','F_Key','Bb_Key','Eb_Key','Ab_Key','Db_Key','Gb_Key','B_Key','E_Key','A_Key','D_Key','G_Key']
signature = ['&c','&b','&bb','&bbb','&bbbb','&bbbbb','&bbbbbb','&#####','&####','&###','&##','&#']
value_name = 'Key_signature'
Key_name = pd.DataFrame(index=KEY, columns=[value_name], data=signature)
Key_name.to_csv("Key_signature.csv", index_label='KEY')
Key_name = pd.read_csv("Key_signature.csv", index_col='KEY')


#%%
import pandas as pd
# 기본음을 추출하는 함수
def extract_base_note(note):
    if '/' in note:
        base_note = note.split('/')[0]  # 슬래시 이전 부분 추출
    else:
        base_note = note
    
    if len(base_note) > 1 and base_note[1] in ['b', '#']:
        return base_note[:2]
    return base_note[0]
#%%
# 코드 타입을 추출하는 함수
import re
def extract_chord_type(note):
    chord_pattern = re.compile(r'[A-G](?:#|b)?(?:m(?:6|7|11|M7)?|M(?:6|7|9)?|dim7?|7(?:sus4)?|sus4|9sus4|add9|6|9|aug(?:7)?|mM7)?(?:\([#b]?(?:[0-9]|1[0-3])\))?(?:/[A-G](?:#|b)?)?')    
    if "/" in note:
        note = note.split("/")[0]
    
    
    match = chord_pattern.match(note)
    if match:
        chord = match.group(0)
        
        if len(chord) > 1 and (chord[1] == 'b' or chord[1] == '#'):
            return chord[2:]
        else:
            return chord[1:]
    
    
    return note


'''
코드의 정규식표현으로 다시 만들어보기 Characteristics_of_chord 이부분
'''


#%%
# def extract_chord_type(note):
#     Characteristics_of_chord = {'m', 'M7', 'm7', '7', "sus4", "7(b9)", "m7(b5)", "dim", "7(#9)","M9","m9"}
    
#     if "/" in note:
#         note = note.split("/")[0]
        
#     for characteristic in Characteristics_of_chord:
#         if characteristic in note:
#             if note[1] == 'b' or note[1] == '#':
#                 return note[2:]
#             else:
#                 return note[1:]    
#     return note
#%% # key에 따라 로마숫자로 변형
def process_key(key, chords, Major_scale):
    # key_formatted = f"{key.strip()}_Key"
    roman_chords = []
    for chord_pair in chords:
        romanized_chord_pair = []

        for note in chord_pair:
            base_note = extract_base_note(note)
            chord_type = extract_chord_type(note)
            found = False

            for col_name in Major_scale.columns:
                if Major_scale.loc[key, col_name] == base_note:
                    roman_numeral = col_name
                    inversion_info = note.split('/')[1] if '/' in note else ''
                    chord_notation = f"{roman_numeral}{chord_type}" if base_note != chord_type else roman_numeral
                    if inversion_info:
                        romanized_chord_pair.append(f"{chord_notation}/{inversion_info}")
                    else:
                        romanized_chord_pair.append(chord_notation)

                    found = True
                    break

            if not found:
                romanized_chord_pair.append(note)

        roman_chords.append(romanized_chord_pair)

    return roman_chords

#%% 메인코드
def harmonics(chords,key_name):
    roman_chords_dict = {}
    secondary_chords = []
    Major_scale = pd.read_csv("Major_scale.csv", index_col='KEY')
    # modulation = input("Key를 입력해주세요 \n(변조가 있으면 , Key를 입력해주세요) : ").split(",")
    # modulation = [key.strip() for key in modulation]  

    for key in key_name:        
        roman_chords = process_key(key, chords, Major_scale)
        roman_chords_dict[key] = roman_chords
        
    if len(key_name) > 1:    
        key1 = key_name[1]    
        chords = roman_chords_dict[key_name[0]]
        secondary_chords = process_key(key1, chords, Major_scale)     
    
    
    return roman_chords_dict, secondary_chords
