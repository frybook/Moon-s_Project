# 리턴값이 없는 함수 = 행동만 하는 함수
# 리턴값이 있는 함수 = 뭔가 돌려주는 함수
# 리턴값 = 사용 가능한 재료 


def myfun1(l):
    l2 = []
    for i in l:
        l2.append(i*2)
    return l2
l = [1,2,3]
myfun1(l)