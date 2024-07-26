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

# 코드 패턴
target_seqs = [
    [43, 36, 17, 34, 15, 1, 18, 8], 
    [6, 1, 15, 32, 1, 20, 31], 
    [1, 22, 6, 32, 1], 
    [6, 32, 17, 22], 
    [22, 17, 15, 32], 
    [17, 22, 15, 32], 
    [1, 17, 6], 
    [1, 18, 1, 18], 
    [22, 15, 32, 1, 29], 
    [22, 58, 22, 6], 
    [1, 1, 6, 18, 1, 25, 6], 
    [1, 8, 22, 17, 6, 1, 15, 32],
    [1, 62, 15, 32], 
    [1, 62, 15, 67, 17, 22, 15, 32, 1]]
# 곡 진행
large_seq = [6, 8, 1, 1, 6, 8, 3, 3, 6, 8, 22, 6, 8, 1, 15, 8, 1, 8, 22, 15, 8, 1, 8, 22, 6, 8, 8, 22, 17, 6, 17, 22, 6, 8, 8, 15, 11, 6, 8, 22, 6, 8, 22, 15, 8, 1, 6, 15, 8, 8, 1, 8, 22, 6, 8, 8, 22, 17, 6, 17, 22, 6, 8, 8, 15, 8, 8, 6, 8, 1, 6, 8, 22, 3, 3, 6, 1, 17, 22, 8, 8, 22, 1, 6, 17, 22, 17, 6, 17, 22, 6, 8, 8, 15, 8, 8, 7, 6, 8, 1, 1, 6, 8, 22, 3, 3, 6, 6, 15, 17, 6, 15, 17, 22, 7]


results = []
order_weight = 10  # 정확도 단위 조절
for target_seq in target_seqs:
    best_match, best_ratio = find_best_match_custom(target_seq, large_seq, order_weight)
    results.append((target_seq, best_match, best_ratio))
    print(f'코드 패턴: {target_seq}')
    print(f'곡에서 진행: {best_match}')
    print(f'정확도: {best_ratio:.2f}')
    print('---')