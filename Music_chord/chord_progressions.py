from chord_progressions_info import chord_pattern
import pandas as pd
#%%
# 검증용 데이터 셋
# roman = ['Ⅰ', 'ⅶm7(b5)', 'ⅲ7', 'ⅵm', 'Ⅴm', 'Ⅰ', 'Ⅳ', 'ⅲm', '#ⅱ7', 'ⅱm', '#Ⅰ', 'Ⅴ', 'Ⅰ', 'ⅶm7(b5)', 'ⅲ7', 'ⅲ7', 'ⅵm', 'Ⅴm', 'Ⅰ7', 'Ⅰ', 'Ⅳ', 'ⅣmM7', 'ⅲm', 'ⅵ7', 'ⅱm', 'Ⅴ7', 'Ⅰ', 'ⅶm7(b5)', 'ⅲ7', 'ⅵm', 'Ⅴm', 'Ⅰ7', 'Ⅰ7', 'Ⅳ', 'ⅣmM7', 'ⅲm', 'ⅵ7', 'ⅱm', 'Ⅴ7', 'Ⅰ', 'ⅶm7(b5)', 'ⅲ7', 'ⅵm', 'Ⅴm', 'Ⅰ7', 'Ⅴ', 'Ⅳ', 'ⅣmM7', 'ⅲm', 'ⅵ7', 'ⅱm', 'Ⅴ7', 'Ⅰ', 'ⅶm7(b5)', 'ⅲ7', 'ⅵm', 'Ⅴm', 'Ⅰ7', 'Ⅰ', 'Ⅳ', 'ⅣmM7', 'ⅲm', '#ⅱ7', '#Ⅴ', 'Ⅴ7', 'Ⅳ', 'Ⅳm', 'ⅲm', 'ⅵ7', 'ⅱm', 'Ⅰ', 'Ⅳ', '#Ⅳm7(b5)', 'Ⅴ', 'Ⅴ', 'Ⅰ', 'Ⅰ', 'ⅶm7(b5)', 'ⅲ7', 'ⅵm', 'Ⅴm', 'Ⅰ', 'Ⅳ', 'ⅲm', 'ⅵm', 'ⅱm', 'Ⅴ7', 'Ⅰ', 'ⅶm7(b5)', 'ⅲ7', 'ⅵm', 'Ⅰ', 'Ⅴm', 'Ⅳ', 'ⅣmM7', 'Ⅰ', 'Ⅳ', 'Ⅰ', '#ⅱ', 'ⅱm', 'ⅱm', 'Ⅴ7', 'Ⅰ', 'Ⅰm', 'ⅱm', '#Ⅰ', 'Ⅰ', 'ⅶm', '#ⅵ', 'ⅵ']




#%%
# 토큰화

def token(roman):
    chord_token = pd.read_csv("chord_token.csv", index_col='chord',encoding='utf-8')
    chord_to_token = chord_token['number'].to_dict()
    chord_progressions = chord_pattern()
    tokenized_progressions = [
        [chord_to_token[chord] for chord in progression]
        for progression in chord_progressions]
    
    tokenized_roman = [
        chord_to_token[chord] for chord in roman]
    
    return tokenized_progressions,tokenized_roman



#%%
def custom_similarity(seq1, seq2, order_weight=2):
    matches = 0
    total_weight = 0
    
    for i, elem in enumerate(seq1):
        if elem in seq2:
            j = seq2.index(elem)
            weight = 1 / (abs(i - j) + 1)  # 올바른 위치로부터의 거리에 따라 페널티 부여
            matches += weight
            total_weight += 1

    # 가중치에 따라 일치 개수 조정
    adjusted_matches = matches * order_weight
    max_length = max(len(seq1), len(seq2))
    similarity_ratio = adjusted_matches / max_length
    
    return similarity_ratio
#%%
def find_best_match_custom(target, sequence, order_weight=2):
    best_ratio = 0
    best_match = None
    target_len = len(target)
    
    for i in range(len(sequence) - target_len + 1):
        subseq = sequence[i:i + target_len]
        ratio = custom_similarity(target, subseq, order_weight)
        
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = subseq
    
    return best_match, best_ratio

#%%


def target_song(tokenized_progressions, tokenized_roman):
    # 코드 패턴
    target_seqs = tokenized_progressions
    # 곡 진행
    large_seq = tokenized_roman   
    results = []
    order_weight = 10  # 정확도 단위 조절

    for target_seq in target_seqs:
        best_match, best_ratio = find_best_match_custom(target_seq, large_seq, order_weight)
        if best_ratio <= 8:
            
            results.append((target_seq, best_match, best_ratio))
            # print(f'코드 패턴: {target_seq}')
            # print(f'곡에서 진행: {best_match}')
            # print(f'정확도: {best_ratio:.2f}')
            # print('---')
    if not results:  # results가 비어있는 경우
        print("비슷한 유형을 찾지 못했습니다.")
    return results

#%%
def convert_data(data):
    converted_data = []
    chord_token = pd.read_csv("chord_token.csv", index_col='chord',encoding='utf-8')
    chord_to_token = chord_token['number'].to_dict()
    token_to_chord = {v: k for k, v in chord_to_token.items()}
    for progression in data:
        chord_progression, best_match, ratio = progression
        
        # 리스트 안의 숫자들을 로마 숫자로 변환
        converted_chord_progression = [token_to_chord.get(token, token) for token in chord_progression]
        converted_best_match = [token_to_chord.get(token, token) for token in best_match]
        
        # 변환된 리스트와 float 값으로 새로운 튜플 생성
        converted_data.append((converted_chord_progression, converted_best_match, ratio))
    
    return converted_data