def print_max(a,b,c):
    if b < a > c:
        print(f"가장큰값은 {a}입니다.")
    elif b > a and b > c:                # and인 이유는 
        print(f"가장큰값은 {b}입니다.")  # or일 경우 a>b큰데 c<a 크지 않을수 있으므로
    else:
        print(f"가장큰값은 {c}입니다.")
print(print_max(10, 22,12))
#%%
def print_max(a, b, c) :
    max_val = 0           # max_val의 값이 0으로 시작
    if a > max_val :      # 0보다 a가 크면
        max_val = a       # max_val을 a 값으로
    if b > max_val :      # a값으로 바뀐 max_val보다 b가 크면 
        max_val = b       # max val을 b 값으로
    if c > max_val :      
        max_val = c
    print(max_val)        # 최종적으로 바뀐 max_val을 값으로 출력한다.
print_max(10,12,30)