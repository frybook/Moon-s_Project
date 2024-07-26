print("="*50)
print("안녕하세요.\n저희 리트리멍에 오신걸 환영 합니다.\n저희 카페는 중대형견만 이용 가능합니다.\n 이용원칙은 1인 1음료가 원칙입니다.")
print("강아지는 최대 2마리까지 무료 입장이 가능합니다.")
print("강아지 이용 요금 아이들의 몸무게로 나뉩니다.")
print("중형견(5kg~20kg) : 6000원\n대형견(20kg이상) : 7000원")
print("="*50)
impossible = ['도사견','핏불','스태퍼드셔','로트와일러','라이카','진돗개','오브차카','캉갈']
dog1 = 6000 # "중형견"
dog2 = 7000 # "대형견"
c1 = 4000
c2 = 4500
c3 = 5500
c4 = 5000
es = 10 #에스
am  = 10 #아메
va = 10 #바라
dp = 10 #댕푸
i = [] # 결제 금액 내역


#%%
while True:
    print("안녕하세요 저희 카페를 이용하기 위해서 강아지 입장 가능 여부를 확인하겠습니다.")
    dogi = input("강아지의 종류가 어떻게 되시나요? : ")
    if dogi in impossible:
        print("손님의 견종은 저희 카페 이용이 불가능 하십니다.\n죄송합니다.")
        print("다음 손님 도와드리겠습니다.")
        print("==="*30)
        continue
    else:
        print("저희 카페 이용 가능 견종입니다.다음으로 도와드리겠습니다.")
        print("$*****"*18)
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
            cups = int(input("에스프레소 고르셨습니다. 몇잔 주문하시겠습니까?")) # 잔 수
            if es >= cups:
                es -= cups
                total += (c1 * cups) # 주문한 커피 가격
            
            elif es <= cups:
                print("지금 고르신 제품은 품절되었습니다. 죄송합니다.")
                print((f"현재 주문 가능한 수량 {es}잔 남았습니다.")) #
                continue

        elif coffee == "c2": # 커피 종류
            cups = int(input("아메리카노 고르셨습니다. 몇잔 주문하시겠습니까?")) # 잔 수
            if am >= cups:
                am -= cups 
                total += (c2 * cups) # 주문한 커피 가격
            elif am <= cups:
                print("지금 고르신 제품은 품절되었습니다. 죄송합니다.")
                print((f"현재 주문 가능한 수량 {am}잔 남았습니다."))
                continue


        elif coffee == "c3": # 커피 종류
            cups = int(input("바닐라 라떼 고르셨습니다. 몇잔 주문하시겠습니까?")) # 잔 수
            if va >= cups:
                va -= cups
                total += (c3 * cups) # 주문한 커피 가격
            elif va <= cups:
                print("지금 고르신 제품은 품절되었습니다. 죄송합니다.")
                print((f"현재 주문 가능한 수량 {va}잔 남았습니다."))
                continue


        elif coffee == "c4": # 커피 종류
            cups = int(input("댕푸치노 고르셨습니다. 몇잔 주문하시겠습니까?")) # 잔 수
            if dp >= cups:
                dp -= cups
                total += (c4 * cups) # 주문한 커피 가격
            elif dp <= cups:
                print("지금 고르신 제품은 품절되었습니다. 죄송합니다.")
                print((f"현재 주문 가능한 수량 {dp}잔 남았습니다."))
                continue
            
            
        elif coffee == "pass":
            break            
            
#%% 총 결제


    print(f"커피 금액은 {total}입니다.")
    ax = (dogs + total)
    while True:
        Usage_amount = int(input(f"강아지 입장료랑 커피값 더해서\n총 결제 금액은 = {ax}원 입니다.\n금액을 결제해주세요 :  "))
        if Usage_amount < ax or Usage_amount > ax:
            print("결제 금액이 다릅니다.결제 금액을 확인해주세요.")
        else:
            break  
    print(f"{Usage_amount}원 결제 되었습니다. 좋은 시간 되세요~")
    print("*" * 50)
    i.append(ax)
    money = sum(i)
    print("===="*20)
    print(f"현재 {money}원 벌었습니다.")
    print("===="*20)

    
    if es == 0 and am == 0 and va == 0 and dp == 0:
        print("오늘 모든 음료가 떨어져서 이용이 불가합니다.\n감사합니다.")
        break
    if money >= 150000:
        print(f"오늘 장사를 접을까요?\n현재{money}원 벌었습니다.")
        print(f"현재 남아있는 재고는 \n에스프레소{es}잔,\n아메리카노{am}잔,\n바닐라라떼{va}잔,\n멍푸치노{dp}잔")
        save = int(input("계속 장사를 하시려면 1번 아니면 2번을 눌러주세요. : "))
        if save == 1:
            continue
        else:
            print("#====#==="*10)
            print("오늘은 날이 좋아서 일찍 마감 하겠습니다. 찾아주셔서 감사합니다.")
            print("=====/*****/===\**\  /**/====/******/")
            print("====/**/  **/===\**\/**/====/**/     ")
            print("===/******/======\****/====/******/  ") 
            print("==/**/   **/=====/***/====/**/       ")
            print("=/*******/======/***/====/******/    ")
            break
    
    
#%%
# (수정 및 추가 해야될것)
# 결제 금액이 - 가 나오는것 (완료)
# 주문을 섞어서 받을 수 있게 만드는것(완료)
# 결제 금액이 부족한 경우 다시 입력 받을 수 있게 만들것(완료)
# 커피가 부족하면 주문이 안되고 다른것을 주문해 달라고 만들것 (완료)
# 다 팔렸을 경우에 커피 주문을 멈출것 (완료)
# 멈췄을때 총 얼마 팔렸는지 알아보자 (완료)
# 가시화를 조금 더 해줘서 보기 편하게 만든다.(완료)
# 최종적으론 코드를 줄일수 있는것을 찾아볼것
# while 문에서 total 값이 0에서 돌아갔을때 다시 0되는걸 고쳐야된다.(완료)
# 강아지 종류 확인 (완료)