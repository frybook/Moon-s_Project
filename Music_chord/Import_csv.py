import os
import pandas as pd
import re

# Rm이 들어간 csv 파일 전체를 불러오기(중간에 정보를 못찾으면 오류가 나옴)
def csv_text():
    # 폴더 경로 설정
    folder_path = "C:\Python\Syntex\working\개인\악보\분석"
    
    # 폴더 내의 "Rm"이 들어간 모든 .csv 파일 이름 가져오기
    file_names = [f for f in os.listdir(folder_path) if f.endswith('.csv') and 'All_Rm' in f]
    
    # 사전 형태로 데이터프레임 저장
    dataframes = {}
    for file_name in file_names:
        file_path = os.path.join(folder_path, file_name)
        # 파일 확장자를 제거하여 변수 이름으로 사용
        variable_name = os.path.splitext(file_name)[0]
        df = pd.read_csv(file_path, encoding='utf-8', header=None)
        # 모든 컬럼 이름을 'chord'로 변경
        df.columns = ['chord'] * len(df.columns)
        dataframes[variable_name] = df
    
    
    return dataframes

Rm_chord_frames = csv_text()
song_list = list(Rm_chord_frames.keys())

#%%

def select_songs(Rm_chord_frames,song_list):    
    num = int(input("곡의 번호를 선택해주세요 : "))
    index_position = num # 0번쨰 인덱스 찾으려고
    song_list = list(Rm_chord_frames.keys()) # 이름들을 인덱스로 찾을수있게 순서를 만들어줌
    selected_key_by_index = song_list[index_position] # 0번의 인덱스에 해당하는 이름이 뭔지 찾음
    selected_df_by_index = Rm_chord_frames[selected_key_by_index] # 찾은이름을 토대로 안에 내용을 꺼냄
    chords_by_index = selected_df_by_index['chord'].tolist() # 찾은 내용을 리스트로 만들어줌
    
    new_chord_list = []
    for chord in chords_by_index:
        new_chords = chord.split()
        new_chord_list.extend(new_chords)
    return new_chord_list
#%%

def select_song(Rm_chord_frames, index_position):
    song_list = list(Rm_chord_frames.keys())  # 이름들을 인덱스로 찾을 수 있게 순서를 만들어줌
    selected_key_by_index = song_list[index_position]  # 인덱스에 해당하는 이름을 찾음
    selected_df_by_index = Rm_chord_frames[selected_key_by_index]  # 찾은 이름을 토대로 내용을 꺼냄
    chords_by_index = selected_df_by_index['chord'].tolist()  # 내용을 리스트로 만듦
    
    new_chord_list = []
    for chord in chords_by_index:
        new_chords = chord.split()
        new_chord_list.extend(new_chords)
    
    return new_chord_list
#%%


def extract_roman_numerals(chords):
    extracted_chords = []
    for chord in chords:
        # 여러 곡들의 패턴의 평균화를 위해서 m,(b5),7위주로 패턴파악과 특수한 dim 추출 
        if re.match(r'^[#b]?[ⅠⅱⅲⅣⅤⅵⅶ]', chord):
            match = re.match(r'^([#b]?[ⅠⅱⅲⅣⅤⅵⅶ])(m7\(b5\)|mM7|m7|m|7|dim)?', chord)
            if match:
                roman_numeral = match.group(1)
                extension = match.group(2)
                if extension == '7':
                    extracted_chords.append(f"{roman_numeral}7")
                elif extension == 'm7(b5)':
                    extracted_chords.append(f"{roman_numeral}m7(b5)")
                elif extension in ['m', 'm7',]:
                    extracted_chords.append(f"{roman_numeral}m")
                elif extension in ['mM7']:
                    extracted_chords.append(f"{roman_numeral}mM7")    
                elif extension == 'dim':
                    extracted_chords.append(f"{roman_numeral}dim")
                else:
                    extracted_chords.append(roman_numeral)
        else:
            extracted_chords.append(chord) # 로마로 표기되지않은 오류들 그대로 출력
    trans7 = []
    for five in extracted_chords:
        if five == "Ⅴ":
            trans7.append(f"{five}7")
        else:
            trans7.append(five)
    return trans7

# 최소 필요 정보
new_chord_list = ['ⅠM7', 'ⅵsus4', 'ⅱm7','Ⅴ9','Ⅴ', 'Ⅴsus4', 'ⅲm7', 'ⅵ7', 'ⅱm7', 'ⅱ']
# 여기서 Ⅴ일 경우 7를 붙이도록 변경

roman_numerals = extract_roman_numerals(new_chord_list)
trans7 = []
for five in roman_numerals:
    if five == "Ⅴ":
        trans7.append(f"{five}7")
    else:
        trans7.append(five)

print(roman_numerals)



#%%%

"""
지금 로마에 포함안되는경우는 그냥 제외해서 출력하고있음 수정해야 됌(해결)
그냥 순수하게 반복되는 애들을 출력해서 모은 데이터를
한번더 가공하는게 낫나? 아니면 지금 가공해서 출력하는게 낫나?
전자일 경우에는 좀더 자세한 텐션까지를 알수있을때 도움이될꺼같고
후자일 경우 진행만을 목적으로 확인하기에는 도움이 될꺼같다.

생각해보닌까 패턴 찾는데 변형된걸 찾는거보다 원래 코드에서 찾는게 낫지 않을까?

패턴의 정형화
- 같은 코드가 나올경우 무시
- 앞에 코드와 무시할수있는 


아니면 아에 
순차진행이 있나 파악하고
2 5 1 인구간이 있나
이런식으로 나눠서 패턴을 파악하는 방식으로 
나중에 이걸 토대로 합치는 방식으로 접근하는 방법



"""
#%%
"""
from collections import defaultdict
def find_repeated_segments(music_text):
    repeats = defaultdict(int)

    # 4~8까지 반복만 설정
    for length in range(4, 9):
        # 슬라이딩 윈도우를 사용하여 현재 길이의 세그먼트를 추출
        for i in range(len(music_text) - length + 1):
            segment = tuple(music_text[i:i + length])
            repeats[segment] += 1

    # 반복되지 않는 세그먼트 필터링
    repeats = {k: v for k, v in repeats.items() if v > 1}

    # Find the most frequently repeated segment
    if repeats:
        most_frequent_segment = max(repeats, key=repeats.get)
        most_frequent_count = repeats[most_frequent_segment]
    else:
        most_frequent_segment = None
        most_frequent_count = 0

    # 가장 자주 반복되는 세그먼트 찾기
    most_frequent_repeats = {
        k: v for k, v in repeats.items() if v == most_frequent_count
    }

    return most_frequent_repeats

# 반복되는 패턴 찾기
repeated_segments = find_repeated_segments(roman_numerals)
print(repeated_segments)
"""