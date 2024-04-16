coffee = 10
print("커피 가격은 300원 입니다.") # 가격
while True:
    cups = int(input("주문할 커피 수량을 말해주세요 :")) # 커피수량
    if cups > coffee:
        print(f"커피가{coffee}수만큼 남았습니다.""\n다시 주문해주세요.")
        continue
    z = int(cups*300) # 주문한 금액
    print(f"총 {z}원 입니다.")
    money = int(input("돈을 넣어주세요 :")) # 주문을 받기
    
    if money >= z :  # 참일 경우  커피준다
        print(f"커피가{cups}잔 나왔습니다.")
        coffee -= cups
        if money > z :
            x = (money-(300*cups))# 초과된 돈
            print(f"거스름돈은{x}원 입니다.")
            coffee -= cups
    
    else:
        y = (cups*300-money)
        print(f"{y}원이 모자랍니다.")
    if coffee <= 0 :
        print("커피가 모두 떨어졌습니다.")
        break