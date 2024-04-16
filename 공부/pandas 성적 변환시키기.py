# 총점 , 평균을 구하고 알파벳 시험 점수 로 만들기


import pandas as pd


data = pd.DataFrame([["짱구",50,45,40,30],
                      ["철수",100,100,80,90],
                      ["맹구",80,80,100,60],
                      ["유리",60,100,60,80],
                      ["훈이",30,20,10,30]],
                     columns =["이름","국어","영어","수학","과학"])

name = data.set_index("이름")

name.loc[:,["총합"]] = name.loc[:,"국어":"과학"].sum(axis = 1)

score = name.copy()
print(name)
'''
     국어   영어   수학  과학   총합
이름                        
짱구   50   45   40  30  165
철수  100  100   80  90  370
맹구   80   80  100  60  320
유리   60  100   60  80  300
훈이   30   20   10  30   90

'''

# for x in range(len(name)):
    
#%%

def ax(x):
    if 80<= x <=100:
        return "A"
    
    elif 60<= x < 80:
        return "B"
    
    elif 40<= x < 60:
        return "C"
    
    elif 20 <= x < 40:
        return  "D"
    
    else:
        return x == "Fail"
    
score["국어"] = score["국어"].apply(ax)
score["영어"] = score["영어"].apply(ax)
score["수학"] = score["수학"].apply(ax)
score["과학"] = score["과학"].apply(ax)
"""
def ad(x):
    score = 0
    if x == "A" :
        score += 5
    return score
    
    if x == "B":
        score += 4
    return score
    
    if x == "C":
        score += 3
    return score

    if x == "D":
        score += 2
    return score

    if x == "Fail":
        score += 1
    return score

    if 18 < x < 20:
        return "A"
    elfif 12 < x 17:
        return "B"
"""

# 

'''
for x in range(len(ndf)): # 행의 갯수
    rows = ndf.iloc[x, :] # 하나의 행을 추출
    tot = 0
    for val in rows: # 칼럼 1개씩 탐색하면 누적
        tot += val
    ndf.iloc[x,4] = tot        # 총점
    ndf.iloc[x,5] = tot // cnt # 평균
'''
# new_data = pd.concat([name,score])
