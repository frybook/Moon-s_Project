import os
import pandas as pd

# Og이 들어간 csv 파일 전체를 불러오기(중간에 정보를 못찾으면 오류가 나옴)
def csv_text():
    # 폴더 경로 설정
    folder_path = "C:\Python\Syntex\working\개인\악보\분석"
    
    # 폴더 내의 "Rm"이 들어간 모든 .csv 파일 이름 가져오기
    file_names = [f for f in os.listdir(folder_path) if f.endswith('.csv') and 'Og' in f]
    
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


Og_chord_frames = csv_text()

#%%
index_position = 6    # 0번쨰 인덱스 찾으려고
song_list = list(Og_chord_frames.keys()) # 이름들을 인덱스로 찾을수있게 순서를 만들어줌
selected_key_by_index = song_list[index_position] # 0번의 인덱스에 해당하는 이름이 뭔지 찾음
selected_df_by_index = Og_chord_frames[selected_key_by_index] # 찾은이름을 토대로 안에 내용을 꺼냄
chords_by_index = selected_df_by_index['chord'].tolist() # 찾은 내용을 리스트로 만들어줌
#%%
new_chord_list = []
for chord in chords_by_index:
    new_chords = chord.split()
    new_chord_list.extend(new_chords)


#%%
import re
from collections import defaultdict


def extract_roman_numerals(chords):
    extracted_chords = []
    for chord in chords:
        # 여러 곡들의 패턴의 평균화를 위해서 m,(b5),7위주로 패턴파악과 특수한 dim 추출 
        if re.match(r'^[A-G][#b]?', chord):
            # Matching the chord structure with optional extension patterns
            match = re.match(r'^([A-G][#b]?)(m7\(b5\)|m7|m|7|dim)?', chord)
            if match:
                root = match.group(1)
                extension = match.group(2)
                if extension == '7':
                    extracted_chords.append(f"{root}7")
                elif extension == 'm7(b5)':
                    extracted_chords.append(f"{root}m7(b5)")
                elif extension in ['m', 'm7']:
                    extracted_chords.append(f"{root}m")
                elif extension == 'dim':
                    extracted_chords.append(f"{root}dim")
                else:
                    extracted_chords.append(root)
        else:
            extracted_chords.append(chord)
    return extracted_chords

origin_numerals = extract_roman_numerals(new_chord_list)
print(origin_numerals)
['B', 'G#m', 'G#m', 'C#', 'C#dim', 'B', 'G#m', 'Cdim', 'C#', 'Em',
 'D#m', 'G#m', 'Em', 'B', 'C#', 'Em', 'F#', 'B', 'G#m', 'Fm7(b5)',
 'Em', 'B', 'G#m', 'Fm7(b5)', 'Em', 'B', 'G#m', 'Fm7(b5)', 'Em', 'B',
 'G#m', 'Em', 'B', 'G#m', 'Fm7(b5)', 'Em', 'B', 'Fm7(b5)', 'G#m', 'Em',
 'D#m', 'G#m', 'Em', 'B', 'Fm7(b5)', 'C#', 'F#', 'B', 'G#m', 'Fm7(b5)',
 'Em', 'B', 'G#m', 'Fm7(b5)', 'Em', 'B', 'G#m', 'Fm7(b5)', 'Em', 'B', 
 'G#m', 'Em', 'B', 'D#m', 'G#m', 'C#', 'C#m', 'F#', 'G', 'C', 'Am',
 'F#m7(b5)', 'Fm', 'C', 'Am', 'F#m7(b5)', 'Fm', 'C', 'Am', 'F#m7(b5)',
 'Fm', 'C', 'G#', 'Am', 'D7', 'Dm', 'Em', 'Dm', 'Fm', 'Fm', 'Fm', 'C',
 'Am', 'D', 'Ddim', 'C', 'Am', 'D7', 'Ddim']
#%%
# 중보되는 코드 삭제
def replace_consecutive_duplicates(chords):
    if not chords:
        return []
    
    result = [chords[0]]  # Initialize with the first chord
    for chord in chords[1:]:
        if chord == result[-1]:
            result.append('')
        else:
            result.append(chord)
    return result

result_numerals =replace_consecutive_duplicates(origin_numerals)
#%%



#%%

# 반복 패턴 찾기
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

repeated_segments = find_repeated_segments(result_numerals)