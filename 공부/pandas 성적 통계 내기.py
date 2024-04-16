import pandas as pd
import numpy as np

def total(*a):
    x = 0
    for i in a:
        x += i
    return x
    

data = [["영수",100,70,20,30],
       ["영희",100,70,20,30],
       ["남수",100,70,20,30],
       ["이수",100,70,20,30]]

info = pd.DataFrame(data,columns= ["이름","국어","수학",'영어',"체육"])

# info["total"] = info["국어","수학","영어","체육"].apply(total)

info["total"] = info.apply(np.sum,axis = 1)

# 이름이 있을때 인덱스로 밀어서 계산을 하는방법
# 범위를 지정해서 계산하는 방법
#  def 함수로 계산하는데 이것도 범위지정가능해야 원하는 답이 나옴
# 가장 이상 적인건 범우 계산하는 방법인거같다.

# https://m.blog.naver.com/jkg57/222477635369