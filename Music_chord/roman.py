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

# "Ⅰ","ⅱ","ⅲ","Ⅳ","Ⅴ","ⅵ","ⅶ"
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
#%% csv 파일 만들기
import csv
def export_to_csv(Roman_chords_list, original_chords_list, key_name, title, export_path):
    csv_file_rm = f"{export_path}_Rm({key_name}).csv"
    csv_file_og = f"{export_path}_Og({key_name}).csv"

    with open(csv_file_rm, mode='w', newline='', encoding='utf-8') as file_rm:
        writer_rm = csv.writer(file_rm)
        for item in Roman_chords_list:
            writer_rm.writerow([item])

    with open(csv_file_og, mode='w', newline='', encoding='utf-8') as file_og:
        writer_og = csv.writer(file_og)
        for item in original_chords_list:
            writer_og.writerow([item])





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



#%%
# 코드 타입을 추출하는 함수
import re
def extract_chord_type(note):    
    # chord_pattern = re.compile(r'[A-G](?:#|b)?(?:m(?:6|7|11|M7)?|M(?:6|7|9)?|dim7?|7(?:sus4)?|sus4|9sus4|add9|6|9|aug(?:7)?|mM7)?(?:\([#b]?(?:[0-9]|1[0-3])\))?(?:/[A-G](?:#|b)?)?')    
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


#%% # key에 따라 로마숫자로 변형
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

                # Convert base_note to Roman numeral
                for col_name in Major_scale.columns:
                    scale_value = Major_scale.at[key, col_name]

                    if scale_value == base_note:
                        roman_numeral = col_name
                        chord_notation = f"{roman_numeral}{chord_type}" if base_note != chord_type else roman_numeral
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
                        scale_value = Major_scale.at[key, col_name]
                        if scale_value == inversion_note:
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

#%% 메인코드
def harmonics(Order_of_keys, chords):
    Major_scale = pd.read_csv("Major_scale.csv", index_col='KEY')
    Roman_symbols =  process_key(Order_of_keys, chords, Major_scale)
    chords_list = [item for sublist in Roman_symbols for item in sublist]
    original_chords_list = []
    for key in chords:
        original_chords_list.extend(chords[key])
    return chords_list,original_chords_list 
