from pdf_chord_extraction_functionalization import text_setting, text_chords, Find_chords
from roman import harmonics
from music_pattern import texting,find_repeated_segments,export_to_csv
from line_filter import line_filter
#%% 곡분석
if __name__ == "__main__":
    lines,key_name,title = text_setting()
    cleaned_lines = text_chords(lines)
    text_separation,change_indices,Order_of_keys = line_filter(cleaned_lines)
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

#%%

Major_scale = pd.read_csv("Major_scale.csv", index_col='KEY')

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
                scale_value = Major_scale.at[key, col_name]

                if scale_value == base_note:
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

        romanized_chord_list.append(' '.join(romanized_chord_pair))

    roman_chords.append(romanized_chord_list)
    
# 리스트안에 리스트를 한곳으로 모으기
chords_list = [item for sublist in roman_chords for item in sublist]

# 딕셔너리안에 리스트를 한곳으로 모으기
original_chords_list = []
for key in chords:
    original_chords_list.extend(chords[key])



