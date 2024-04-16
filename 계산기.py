# 클래스 함수 선언
class Calc() :

    def __init__(self) : # __init__ 함수로 선택 목록을 인스턴스 실행시 보여준다.
        print("\n"
              ":: 사칙 연산 ::\n"
              "===========================\n"
              "1.더하기(+)\n"
              "2.빼기(-)\n"
              "3.곱하기(*)\n"
              "4.나누기(/)\n"
              "0.Quit\n"
              "===========================\n")

    def plus(self, num1, num2) : # 더하기 함수
        self.num3 = num1 + num2
        return self.num3

    def minus(self, num1, num2) : # 빼기 함수
        self.num3 = num1 - num2
        return self.num3
    

    def multiple(self, num1, num2): # 곱하기 함수
        self.num3 = num1 * num2
        return self.num3

    def divide(self, num1, num2): # 나누기 함수
        self.num3 = num1 / num2
        return self.num3


def On_Off() : # 반복문에서 종료, 재시작을 선택하는 함수
    result = int(input("\n"
                       "Off(1) - 종료 / On(2) - 재시작 : "))
    if result == 2:
        pass
    elif result == 1:
        print("종료합니다.")
        exit() # 종료하는 함수


while True :
    calc = Calc()

    N = int(input("목록에서 값을 구할 사칙 연산 번호를 입력해주세요 : "))

    if N == 1 :
        try : # 에러가 없으면 아래 내용을 시도한다.
            num1, num2 = map(int, input("수식을 입력하세요(a+b) : ").split("+"))
            print(f"{num1} + {num2} = {calc.plus(num1, num2)}") # calc.plus(num1, num2) 클래스 안에 있는 더하기 메소드 실행

        except : # 위에 내용이 에러가 있으면 아래 내용을 시도한다.
            print("\n"
                  "수식을 잘못 입력했습니다.\n"
                  "\n"
                  "재시작 할까요?")
            pass

        On_Off() # 반복문에서 종료, 재시작을 선택하는 함수

    if N == 2 :
        try : # 에러가 없으면 아래 내용을 시도한다.
            num1, num2 = map(int, input("수식을 입력하세요(a-b) : ").split("-"))
            print(f"{num1} - {num2} = {calc.minus(num1, num2)}") # calc.minus(num1, num2) 클래스 안에 있는 빼기 메소드 실행

        except : # 위에 내용이 에러가 있으면 아래 내용을 시도한다.
            print("\n"
                  "수식을 잘못 입력했습니다.\n"
                  "\n"
                  "재시작 할까요?")
            pass

        On_Off() # 반복문에서 종료, 재시작을 선택하는 함수

    if N == 3 : # 에러가 없으면 아래 내용을 시도한다.
        try :
            num1, num2 = map(int, input("수식을 입력하세요(a*b) : ").split("*"))
            print(f"{num1} * {num2} = {calc.multiple(num1, num2)}") # calc.multiple(num1, num2) 클래스 안에 있는 곱하기 메소드 실행

        except: # 위에 내용이 에러가 있으면 아래 내용을 시도한다.
            print("\n"
                  "수식을 잘못 입력했습니다.\n"
                  "\n"
                  "재시작 할까요?")
            pass

        On_Off() # 반복문에서 종료, 재시작을 선택하는 함수

    if N == 4 :
        try : # 에러가 없으면 아래 내용을 시도한다.
            num1, num2 = map(int, input("수식을 입력하세요(a/b) : ").split("/"))
            print(f"정답 : {num1} / {num2} = {calc.divide(num1, num2)}") # calc.divide(num1, num2) 클래스 안에 있는 나누기 메소드 실행

        except: # 위에 내용이 에러가 있으면 아래 내용을 시도한다.
            print("\n"
                  "수식을 잘못 입력했습니다.\n"
                  "\n"
                  "재시작 할까요?")
            pass

        On_Off() # 반복문에서 종료, 재시작을 선택하는 함수

    elif N == 0 :
        print("종료합니다.")
        break

    else :
        print("재시작 합니다.")
#%%Calc()
# 다른파일에서도 사용가능
from 계산기 import Calc
