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

Frame.columns
A = Frame.loc['Gb_Key']

#%%
c = ["D","Db","F","C","F#"]
for idx, key in enumerate(A):
    for f in c:
        if key[0] == f:
            print(f)


#%%
from pdf_chord_extraction_functionalization import text_setting, text_chords, Find_chords
from line_filter import line_filter
import os
#%% 곡분석
if __name__ == "__main__":
    folder_path = "C:/Python/Syntex/working/개인/악보" # 악보 폴더 위치
    title = input("곡 제목을 말해주세요 :")
    file_path = os.path.join(folder_path, f"{title}.pdf")
    lines,key_name,title = text_setting(file_path)
    cleaned_lines = text_chords(lines)
    text_separation,change_indices,Order_of_keys = line_filter(cleaned_lines,key_name)
    chords = Find_chords(text_separation) 
#%%
import pandas as pd
# 기본음을 추출하는 함수 베이스음 
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
    chord_pattern = re.compile(r'[A-G](?:#|b)?(?:m(?:6|7|9|11|M7)?|M(?:6|7|9)?|dim7?|7(?:sus4)?|sus4|9sus4|add9|6|9|aug(?:7)?|mM7|(?:add9))?(?:\([#b]?(?:[0-9]|1[0-3]|add9)\))?(?:/[A-G](?:#|b)?)?')
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
            
Major_scale = pd.read_csv("Major_scale.csv", index_col='KEY') 
All_Major_scale = pd.read_csv("All_Major_scale.csv", index_col='KEY')       
#%%
def process_key(Order_of_keys, chords, Major_scale):
    roman_chords = []
    for idx, key in enumerate(Order_of_keys):
        chord_list = chords[idx]
        romanized_chord_list = []

        for chord_pair in chord_list:
            romanized_chord_pair = []

            for note in chord_pair.split():
                base_note = extract_base_note(note)
                chord_type = extract_chord_type(note)
                found = False

                for col_name in Major_scale.columns:
                    scale_values = Major_scale.at[key, col_name].split(',')
                    if base_note in scale_values:
                        roman_numeral = col_name
                        chord_notation = f"{roman_numeral}{chord_type}" if chord_type else roman_numeral
                        found = True
                        break

                if not found:
                    romanized_chord_pair.append(note)
                    continue

                inversion_info = ''
                if '/' in note:
                    inversion_note = note.split('/')[1]
                    inversion_found = False
                    for col_name in Major_scale.columns:
                        scale_values = Major_scale.at[key, col_name].split(',')
                        if inversion_note in scale_values:
                            inversion_info = col_name
                            inversion_found = True
                            break
                    if not inversion_found:
                        inversion_info = inversion_note

                if inversion_info:
                    romanized_chord_pair.append(f"{chord_notation}/{inversion_info}")
                else:
                    romanized_chord_pair.append(chord_notation)

            romanized_chord_list.append(' '.join(romanized_chord_pair))

        roman_chords.append(romanized_chord_list)

    return roman_chords

"""위치는 찾았고 이제 그 위치를 로마로 변환할수있는 알고리즘이 필요"""

#%%

def harmonics(Order_of_keys, chords):
    Major_scale = pd.read_csv("Major_scale.csv", index_col='KEY')
    All_Major_scale = pd.read_csv("All_Major_scale.csv", index_col='KEY')
    Roman_symbols =  process_key(Order_of_keys, chords, Major_scale)
    All_Roman_symbols =  process_key(Order_of_keys, chords, All_Major_scale)
    chords_list = [item for sublist in Roman_symbols for item in sublist]
    All_chords_list = [item for sublist in All_Roman_symbols for item in sublist]
    original_chords_list = []
    for key in chords:
        original_chords_list.extend(chords[key])
    return chords_list,original_chords_list,All_chords_list

Roman_chords_list,original_chords_list,All_chords_list = harmonics(Order_of_keys, chords)
