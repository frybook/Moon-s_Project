import pandas as pd
import re




#%%
# 조표가 바뀌는 분기점을 찾고 그 분기점으로 text를 나누는 함수
def line_filter(cleaned_lines):
    Key_name = pd.read_csv("Key_signature.csv", index_col='KEY')
    pattern = '|'.join(re.escape(sig) for sig in Key_name["Key_signature"]) # 패턴만들어서 
    pattern = pattern.replace(r'\&b', r'\&b+') 
    
    filtered = []
    for text_line in cleaned_lines:
        matches = re.findall(pattern,text_line)
        filtered.append(matches)              # 패턴의 맞는 텍스트만 남김
        
    # 키가 바뀔때마다 바뀌는 행을 구함
    change_indices = []
    last_value = None
    for i, current_value in enumerate(filtered):
        if current_value not in ([], last_value):
            change_indices.append(i)
            last_value = current_value
    
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
            
    # 끝을 설정해주고
    text_separation = {}
    change_indices.append(len(cleaned_lines))
    # cleaned_lines에서 조표에 맞춰서 분리
    for i in range(len(change_indices) - 1):
        start_idx = change_indices[i]
        end_idx = change_indices[i + 1]
        text_separation[i] = cleaned_lines[start_idx:end_idx] # i값에다가 key의 이름을 넣으면 될꺼같다.
    
    return text_separation,change_indices,Order_of_keys


'''
딕셔너리로 나눴을때 어떤키인지 인덱스로 추가해야 되겠다.'''