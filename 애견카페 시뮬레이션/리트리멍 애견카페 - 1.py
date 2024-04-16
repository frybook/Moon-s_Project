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
yes = 1
no = 0

es = 10 #에스
am  = 10 #아메
va = 10 #바라
dp = 10 #댕푸
#%%
while True:
    yes = (int(input("메뉴를 보시겠습니까?: \nyes = 1번\nno = 2번\n번호를 골라주세요 : ")))
    if yes == 1:
    	print("="*50)
    	print("Espresso(c1) : 4000\nAmericano(c2) : 4500\nVanilla Latte(c3) : 5500\n$Dangppuccino$(c4) : 5000$\n뒤에 적힌 코드로 주문해주세요!")
    	print("="*50)
    else :
        pass
    print(f"현재 주문 가능한 커피는\nEspresso(c1) : {es}잔\nAmericano(c2) : {am}잔\nVanilla Latte(c3) : {va}잔\n$Dangppuccino$(c4) : {dp}잔\n주문 가능합니다.")
    dog = int(input("강아지 친구들의 사이즈는 어디에 속하나요?\n 중형견 = 1번 대형견 = 2번\n(없는 경우엔 다른 숫자를 눌러주세요)\n번호를 골라주세요 : "))
#%%
    if dog == 1:
       middle = int(input("아이들은 총 몇 마리일까요?"))
       dogs = (middle - min(middle,2)* dog1) # 2마리는 무료
     
       
    elif dog == 2:
        large = int(input("아이들은 총 몇 마리일까요?"))
        dogs = ((dog2 * large) - 12000) # 2마리는 무료
    
    else:
        dogs == 0
        pass
    coffee = input("주문할 커피 코드를 을 말해주세요 :") # 커피종류
    if coffee == "c1":
    	cups = int(input("에스프레소 주문 받았습니다. 몇잔 주문하시겠습니까?"))
    	if cups <= es:
    		x = int(input(f"{cups}잔 주문하셔서 {c1*cups}원 입니다.\n총 결제 금액은 = {dogs + (c1*cups)}\n금액을 결제해주세요 : "))
    		print(f"{x}원 결제 되었습니다. 즐거운 시간 되세요")
    		es -= cups

    elif coffee == "c2":
    	cups = int(input("아메리카노 주문 받았습니다. 몇잔 주문하시겠습니까?"))
    	if cups <= am:
    		x = int(input(f"{cups}잔 주문하셔서 {c2*cups}원 입니다.\n총 결제 금액 : {dogs + (c2*cups)}\n금액을 결제해주세요 : "))
    		print(f"{x}원 결제 되었습니다. 즐거운 시간 되세요")
    		am -= cups    
    
    elif coffee == "c3":
    	cups = int(input("바닐라 라떼 주문 받았습니다. 몇잔 주문하시겠습니까?"))
    	if cups <= va:
    		x = int(input(f"{cups}잔 주문하셔서 {c3*cups}원 입니다.\n총 결제 금액 : {dogs + (c3*cups)}\n금액을 결제해주세요 : "))
    		print(f"{x}원 결제 되었습니다. 즐거운 시간 되세요")
    		va -= cups
    
    elif coffee == "c4":
    	cups = int(input("댕푸치노 주문 받았습니다. 몇잔 주문하시겠습니까?"))
    	if cups <= dp:
    		x = int(input(f"{cups}잔 주문하셔서 {c4*cups}원 입니다.\n총 결제 금액 : {dogs + (c4*cups)}\n금액을 결제해주세요 : "))
    		print(f"{x}원 결제 되었습니다. 즐거운 시간 되세요")
    		dp -= cups
    
    else:
        pass
    
#%%
# (수정 및 추가 해야될것)
# 결제 금액이 - 가 나오는것
# 주문을 섞어서 받을 수 있게 만드는것
# 결제 금액이 부족한 경우 다시 입력 받을 수 있게 만들것
# 중간에 주문을 취소 가능 하게 만들것
# 커피가 부족하면 주문이 안되고 다른것을 주문해 달라고 만들것
# 다 팔렸을 경우에 커피 주문을 멈출것
# 최종적으론 코드를 줄일수 있는것을 찾아볼것