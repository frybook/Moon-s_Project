def add_many(*ax):
    result = 0
    for i in ax:
        result += i
    return result

print(add_many())
#%%
def add_mul(choice,*args): # *매개변수 이름 앞에 붙이면 튜플로 만듬
    if choice == "add": # 매개변수 chioce에 "add"를 입력받을떼
        result = 0
        for i in args:
            result += i # args에 입력받은 모든값을 더한다.
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i # args에 입력받은 모든값을 곱한다.
    return result

print(add_mul("mul",5,4,3,2,1))

#%%
def say_nick(nick):
    if nick =="바보":
        return           # 만약 바보라는 값이 나오면 리턴 끝이라는 듯
    print("나의 별명은 %s입니다."% nick)

print(say_nick("돈가스"))
#%%
name = input("이름이 뭐에요?")
print(name)

#%%
