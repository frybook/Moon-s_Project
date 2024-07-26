from pdf_chord_extraction_functionalization import text_setting, text_chords, Find_chords
from roman import harmonics
from music_pattern import texting,find_repeated_segments,export_to_csv
import pandas as pd
import re

#%% 곡분석
if __name__ == "__main__":
    lines,key_name,title = text_setting()
    cleaned_lines = text_chords(lines)



#%%

Key_name = pd.read_csv("Key_signature.csv", index_col='KEY')
pattern = '|'.join(re.escape(sig) for sig in Key_name["Key_signature"]) # 패턴만들어서 
pattern = pattern.replace(r'\&b', r'\&b+') 

filtered = []
for text_line in cleaned_lines:
    matches = re.findall(pattern,text_line)
    filtered.append(matches)              # 패턴의 맞는 텍스트만 남김
    
'''
------------여기과정은 나중에 로마에서 다시 key 바꿔서 코드로 만들때 사용하면 될듯
# Key_name에서 받은 값을 가지고 자동으로 그 키를 다시 찾음
Key_name = pd.read_csv("Key_signature.csv", index_col='KEY')

x = []
for s in key_name:
    if s in Key_name.index:
        x.append(Key_name.loc[s,'Key_signature'])

print(y)

# 여기서 언제 처음 나오는지 찾는 과정
index_bbbbbb = None
for i, sublist in enumerate(y):
    if x[0] in sublist:
        index_bbbbbb = (i)
        break


index_amp = None
for i, sublist in enumerate(y):
    if x[1] in sublist:
        index_amp = (i)
        break

'''
'''
생각해야 될게
처음 나온 부분에서 그 전까지부분까지 짜르고 또 그 다음분에서 부터 적용해서 짜르고 이런식으로 하면 좋을꺼같다
1. 전조가 없는경우는 해당이안되기 때문에 해당곡은 제외시키도록 생각
2. 전조가 2번되는 경우 이 경우에는 
'''
#%%

# cl = cleaned_lines[0:25]

change_indices = []

# 키가 바뀔때마다 바뀌는 행을 구함
last_value = None
for i, current_value in enumerate(filtered):
    if current_value not in ([], last_value):
        change_indices.append(i)
        last_value = current_value
# 나온 행에서 ?_key를 다시 구해서 정보를 갖고있게한다.


Key_Trans = []
for i in range(len(change_indices)):
    x = change_indices[i]
    Trans = filtered[x]
    Key_Trans.append(Trans)

# &bb상태에서 다시 ?_key로 바꾸는 과정
Order_of_keys = []
Frame_values = Key_name.values
for information in Key_Trans:
    if information in Frame_values:
        key_name = Key_name.loc[Frame_values == information].index[0]
        Order_of_keys.append(key_name) 
    




text_separation = {}

# 마지막 행을 추가해서 끝을 설정
change_indices.append(len(cleaned_lines))



# 불러낼 리스트의 시작과 끝을 만들어준다
for i in range(len(change_indices) - 1):
    start_idx = change_indices[i]
    end_idx = change_indices[i + 1]   
    text_separation[i] = cleaned_lines[start_idx:end_idx]


    




