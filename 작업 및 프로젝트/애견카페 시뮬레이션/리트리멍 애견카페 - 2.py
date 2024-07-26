print("="*50)
print("안녕하세요.\n저희 리트리멍에 오신걸 환영 합니다.\n저희 카페는 중대형견만 이용 가능합니다.\n 이용원칙은 1인 1음료 2견인 원칙입니다.")
print("강아지 이용 요금 아이들의 몸무게로 나뉩니다.")
print("중형견(5kg~20kg) : 6000원\n대형견(20kg이상) : 7000원")
print("="*50)

dog1 = 6000 # "중형견"
dog2 = 7000 # "대형견"
c1 = 4000
c2 = 4500
c3 = 5500
c4 = 5000
total = 0

es = 10 #에스
am  = 10 #아메
va = 10 #바라
dp = 10 #댕푸
#%%
while True:
    yes = (int(input("메뉴를 보시겠습니까?: \nyes = 1번\nno = 2번\n번호를 골라주세요 : ")))
    if yes == 1:
    	print("="*50)
    	print("Espresso(c1) : 4000원\nAmericano(c2) : 4500원\nVanilla Latte(c3) : 5500원\n$Dangppuccino$(c4) : 5000원\n뒤에 적힌 코드로 주문해주세요!")
    	print("="*50)
    else :
        pass
    print(f"현재 주문 가능한 커피는\nEspresso(c1) : {es}잔\nAmericano(c2) : {am}잔\nVanilla Latte(c3) : {va}잔\n$Dangppuccino$(c4) : {dp}잔\n주문 가능합니다.")
    dog = int(input("강아지 친구들의 사이즈는 어디에 속하나요?\n 중형견 = 1번 대형견 = 2번\n(없는 경우엔 다른 숫자를 눌러주세요)\n번호를 골라주세요 : "))
#%% 강아지 입장료
    if dog == 1:
       middle = int(input("아이들은 총 몇 마리일까요?"))
       dogs = ((middle - min(middle,2))* dog1) # 2마리는 무료
       if dogs < 0:
           dogs = 0
       
    elif dog == 2:
        large = int(input("아이들은 총 몇 마리일까요?"))
        dogs = ((large - min(large,2)) * dog2) # 2마리는 무료
        if dogs < 0:
            dogs = 0
    else:
        dogs = 0
        pass
    if dogs <= 0:
        print("아이들 추가 요금은 없습니다.")
    else:
        print(f"아이들 추가 요금은 {dogs}입니다.")
#%% 커피 값
    total = 0
    while True:
        coffee = input("주문할 커피를 말씀해주세요.없으실 경우 pass : ")
        if coffee == "c1": # 커피 종류
            cups = int(input("에스프레소 주문 받았습니다. 몇잔 주문하시겠습니까?")) # 잔 수
            es -= cups
            total += (c1 * cups) # 주문한 커피 가격


        elif coffee == "c2": # 커피 종류
            cups = int(input("아메리카노 주문 받았습니다. 몇잔 주문하시겠습니까?")) # 잔 수
            am -= cups 
            total += (c2 * cups) # 주문한 커피 가격



        elif coffee == "c3": # 커피 종류
            cups = int(input("바닐라 라떼 주문 받았습니다. 몇잔 주문하시겠습니까?")) # 잔 수
            va -= cups
            total += (c3 * cups) # 주문한 커피 가격



        elif coffee == "c4": # 커피 종류
            cups = int(input("댕푸치노 주문 받았습니다. 몇잔 주문하시겠습니까?")) # 잔 수
            dp -= cups
            total += (c4 * cups) # 주문한 커피 가격

        elif coffee == "pass":
            break            
            
#%% 총 결제
    print(f"커피 금액은 {total}입니다.")
    Usage_amount = int(input(f"총 결제 금액은 = {dogs + total}\n금액을 결제해주세요 :  "))
    print(f"{Usage_amount}원 결제 되었습니다. 좋은 시간 되세요~")
    print("*" * 50)

    
    
#%%
# (수정 및 추가 해야될것)
# 결제 금액이 - 가 나오는것 (완료)
# 주문을 섞어서 받을 수 있게 만드는것(완료)
# 결제 금액이 부족한 경우 다시 입력 받을 수 있게 만들것
# 중간에 주문을 취소 가능 하게 만들것
# 커피가 부족하면 주문이 안되고 다른것을 주문해 달라고 만들것
# 다 팔렸을 경우에 커피 주문을 멈출것
# 멈췄을때 총 얼마 팔렸는지 알아보자
# 가시화를 조금 더 해줘서 보기 편하게 만든다.
# 최종적으론 코드를 줄일수 있는것을 찾아볼것
# while 문에서 total 값이 0에서 돌아갔을때 다시 0되는걸 고쳐야된다.