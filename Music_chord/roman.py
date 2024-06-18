import pandas as pd

KEY = ['C_Key','F_Key','Bb_Key','Eb_Key','Ab_Key','Dd_Key','Gb_Key','B_Key','E_Key','A_Key','D_Key','G_Key']
Chrods_name = {"Ⅰ" : ["C","F",  "Bb", "Eb", "Ab", "Db", "Gb","B", "E", "A", "D", "G"],
               "ⅱ" : ["D","G",  "C",  "F",  "Bb", "Eb", "Ab","C#","F#","B", "E", "A"],
               "ⅲ" : ["E","A",  "D",  "G",  "C",  "F",  "Bb","D#","G#","C#","F#","B"],
               "Ⅳ" : ["F","Bb", "Eb", "Ab", "Db", "Db", "B", "E", "A", "D", "G", "C"],
               "Ⅴ" : ["G","C",  "F",  "Bb", "Eb", "Ab", "Db","F#","B", "E" ,"A", "D"],
               "ⅵ" : ["A","D",  "G",  "C",  "F",  "Bb", "Eb","G#","C#","F#","B", "E"],
               "ⅶ" : ["B","E",  "A",  "D",  "G",  "C",  "F", "A#","D#","G#","C#","F#"]}
Frame = pd.DataFrame(Chrods_name,index = KEY)


# CSV파일로 저장하기
Frame.to_csv("Major_scale.csv", index_label='KEY')

# CSV파일 읽기
Frame = pd.read_csv("Major_scale.csv", index_col='KEY')


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

# 코드 타입을 추출하는 함수
def extract_chord_type(note):
    Characteristics_of_chord = {'m', 'M7', 'm7', '7', "sus4", "7(b9)", "m7(b5)", "dim", "7(#9)"}
    
    if "/" in note:
        note = note.split("/")[0]
        
    for characteristic in Characteristics_of_chord:
        if characteristic in note:
            if note[1] == 'b' or note[1] == '#':
                return note[2:]
            else:
                return note[1:]    
    return note


def harmonics(chords):
    key = input("해당 곡의 Key를 입력해주세요 : ")
    Frame = pd.read_csv("Major_scale.csv", index_col='KEY')
    key = f"{key}_Key"
    roman_chords = []

    for chord_pair in chords:
        romanized_chord_pair = []
        
        for note in chord_pair:
            base_note = extract_base_note(note)
            chord_type = extract_chord_type(note)
            found = False
            
            for col_name in Frame.columns:
                if Frame.loc[key, col_name] == base_note:
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


