from pdf_chord_extraction_functionalization import text_setting, text_chords, Find_chords
from roman import harmonics,export_to_csv
from line_filter import line_filter
#%% 곡분석
if __name__ == "__main__":
    lines,key_name,title = text_setting()
    cleaned_lines = text_chords(lines)
    text_separation,change_indices,Order_of_keys = line_filter(cleaned_lines)
    chords = Find_chords(text_separation)      # 코드 악보
    Roman_chords_list,original_chords_list = harmonics(Order_of_keys, chords) # 로마 악보
    export_to_csv(Roman_chords_list,original_chords_list,key_name,title)
    
    # Transtotext = Transformation_roman[key_name[0]]
    # music_text = texting(Transtotext)
    # music_pattern = find_repeated_segments(music_text)
    # export_to_csv(music_pattern, f'{title}코드.csv')
    
#%%
"""
업데이트 해야 할 내용:    
    제외할 단어 문장을 여러개 지정 가능하게 설정
    영어 가사의 대한 근본적인 문제를 해결(결국 위에도 같은 내용) 좌표로 제외하는 방법 찾음
    (자동 좌표를 찾는걸 만들어야 해결될듯 하다)
    Major or minor 따라 바뀌는 스케일
    전조곡들은 어떻게 설정할지(어느정도 해결)
    전조가 있기전에 &나오고 #,b이 몇개가 붙는지 나온다(해결)
    
    dual funtion은 어떻게 할것인가?
    * 근본적인 문제가 영어 가사의 등장,
    * 분석할때 다른키에서 중복된 key의 값이 같을때 전조했을때 그키의 분석으로해야되는데 전조 전에 키로 분석
    키가 다를 경우 키마다 패턴을 분석한뒤에 합치는게 더 낫지 않을까?

업데이트 한내용
자동으로 key 찾아주기(수리중)
전조곡들의 여부
제외 단어 쉽게 코드화
코드 분리화 수정
전조되는 부분을 나눠서 키와 코드를 분리
original과 roman 를 csv로 저장해서 데이터 수집

"""

#%%

'''
코드 진행 :
    4도 - 3도7 - 6도 : 슬프고 어두운 느낌
    2도 - 5도  - 1도 : 근본
  Boy  
    
    '''

#%%
from collections import defaultdict

def find_repeating_patterns(sequence):
    n = len(sequence)
    patterns = defaultdict(int)
    
    # Check for patterns of different lengths
    for length in range(1, n // 2 + 1):
        for start in range(n - length + 1):
            pattern = tuple(tuple(sublist) for sublist in sequence[start:start + length])
            patterns[pattern] += 1
            
    # Filter out patterns that only occur once
    repeating_patterns = {pattern: count for pattern, count in patterns.items() if count > 1}
    
    return repeating_patterns

repeating_patterns = find_repeating_patterns(A)
print(repeating_patterns)

#%%
def find_longest_repeating_patterns(repeating_patterns):
    # Sort patterns by their length in descending order
    sorted_patterns = sorted(repeating_patterns.keys(), key=len, reverse=True)
    
    # Initialize a set to keep track of indices covered by patterns
    covered_indices = set()
    longest_patterns = []

    for pattern in sorted_patterns:
        pattern_length = len(pattern)
        indices_covered = [tuple(range(i, i + pattern_length)) for i in range(len(pattern))]
        
        # Check if the current pattern overlaps with any already covered indices
        if not any(set(indices).intersection(covered_indices) for indices in indices_covered):
            longest_patterns.append(pattern)
            for indices in indices_covered:
                covered_indices.update(indices)

    return longest_patterns

longest_repeating_patterns = find_longest_repeating_patterns(repeating_patterns)
