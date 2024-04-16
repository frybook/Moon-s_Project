# return 값이 나오면 함수가 종료한다.
def add(a,b):
    print(f"({a})와({b})를 입력 받았습니다.")
    print(f"두 값을 더하면 ({a+b})입니다.")
    return add
temp = add(5, 6)
print(temp)
# print(temp) None
#%%

def f_1(x):   
    return(2*x) +1 # (2 * 10) + 1
print(f_1(10))

def f_2(x):
    return(x**2)+(2*x) + 1 # (10제곱 2) +(2*10)+1
print(f_2(10))
#%%
def myfunc(n):
    print('메세지 1')
    print('메세지 2')
    if n == 0:
        return 0
    print('메세지 3')
    return 1
a = myfunc(0) # 메세지 1, 2, 3이 모두 출력, a에는 1반환
b = myfunc(0) # 메세지 1, 2만 출력, b에는 0 반환
#%%
def coin():
    for i in range(100):
        print("비트코인")
        return # 함수를 탈출해서 한번만 적용됌
print(coin())
#%%
def print_coins():
    for i in range(100):
        print("비트코인")
print(print_coins())