import pandas as pd

df = pd.read_excel("수원시주차창정보표준데이터.xlsx")
df = df.drop(columns=['주차장구분','데이터기준일자'])
public = df['주차구획수'].sum() # 8807
Residents_first = pd.read_csv("수원시_거주자우선주차_정보.csv", encoding='euc-kr')
Residents_first_parking_lot = len(Residents_first.index) # 거주자 우선주차 수
#%% 구 단위로 지역 묶기 , 공영 주차장 수

# 장안구
Jangan_gu_df = df[df['소재지지번주소'].str.contains('장안구', na=False)]
Jangan_gu_sum = Jangan_gu_df['주차구획수'].sum()# 1957
Jangan_gu_parking_lot = len(Jangan_gu_df.index)# 13
# 총 주차장수 13/50*100 = 26%
# 권선구
Gwonseon_gu_df = df[df['소재지지번주소'].str.contains('권선구', na=False)]
Gwonseon_gu_sum = Gwonseon_gu_df['주차구획수'].sum()# 2049
Gwonseon_gu_parking_lot = len(Gwonseon_gu_df.index)# 10
# 총 주차장수 10/50*100 = 20%
# 팔달구
Paldal_gu_df = df[df['소재지지번주소'].str.contains('팔달구', na=False)]
Paldal_gu_sum = Paldal_gu_df['주차구획수'].sum() # 2306
Paldal_gu_parking_lot = len(Paldal_gu_df.index) # 14
# 총 주차장수 14/50*100 = 28%
# 영통구
Yeongtong_gu_df = df[df['소재지지번주소'].str.contains('영통구', na=False)]
Yeongtong_gu_sum = Yeongtong_gu_df['주차구획수'].sum() # 2495
Yeongtong_gu_parking_lot = len(Yeongtong_gu_df.index) # 14
# 총 주차장수 14/50*100 = 28%

#%%
# 수원시 총 인구수
population = pd.read_csv("경기도_수원시 인구현황_20231231.csv", encoding='euc-kr')
population = population.loc[0,"인구2)_계"]
# 21년 지역별 인구수
Suwon_city_population = pd.read_csv("수원시_인구현황.csv", encoding='euc-kr')

# 21년 12월기준 총 인구수
Total_population = Suwon_city_population['인구_합계'].sum() # 1218821
# [(1233424 - 1218821) ÷ 1218821] × 100 = 1.20% 증가 
growth_rate = (((population - Total_population) /Total_population)*100) # 1.1981250733290614
# 21년자료로 구해도 오차율이 낮은걸 알수있다

#%%
# 구 단위 인구수 

# 장안구
Jangan_gu_P = Suwon_city_population[Suwon_city_population['구'].str.contains('장안구', na=False)]
Total_Jangan_gu = Jangan_gu_P['인구_합계'].sum() # 277206
# 권선구
Gwonseon_gu_P = Suwon_city_population[Suwon_city_population['구'].str.contains('권선구', na=False)]
Total_Gwonseon_gu = Gwonseon_gu_P['인구_합계'].sum() # 374195
# 팔달구
Paldal_gu_P = Suwon_city_population[Suwon_city_population['구'].str.contains('팔달구', na=False)]
Total_Paldal_gu = Paldal_gu_P['인구_합계'].sum() # 194619
# 영통구
Yeongtong_gu_P = Suwon_city_population[Suwon_city_population['구'].str.contains('영통구', na=False)]
Total_Yeongtong_gu = Yeongtong_gu_P['인구_합계'].sum() # 372801

#%% 비율 확인 (인구/주차장 수)
# 장안구
Jangan_gu_parking_lot_ratio= Total_Jangan_gu/Jangan_gu_parking_lot
# 21323.53846153846
# 권선구
Gwonseon_gu_parking_lot_ratio=Total_Gwonseon_gu/Gwonseon_gu_parking_lot
# 37419.5
# 팔달구
Paldal_gu_parking_lot_ratio=Total_Paldal_gu/Paldal_gu_parking_lot
# 13901.357142857143
# 영통구
Yeongtong_gu_parking_lot_ratio=Total_Yeongtong_gu/Yeongtong_gu_parking_lot
# 26628.64285714286
'''인구수의 비율당 주차장수의 비례 관계
하지만 거주목적 이외에 직장및여러목적의 관계도 생각해봐야될듯 합니다.'''

#%%
import pandas as pd
building = pd.read_excel("수원시_건물_총괄표제부.xlsx")

#%% 구 별로 주차장수 
Jangan_gu_building = building[building['토지소재지'].str.contains('장안구', na=False)]
Total_parking_lot_J = Jangan_gu_building['총주차수'].sum() # 66904

Gwonseon_gu_building = building[building['토지소재지'].str.contains('권선구', na=False)]
Total_parking_lot_G = Gwonseon_gu_building['총주차수'].sum() # 99211

Paldal_gu_building = building[building['토지소재지'].str.contains('팔달구', na=False)]
Total_parking_lot_P = Paldal_gu_building['총주차수'].sum() # 39167

Yeongtong_gu_building = building[building['토지소재지'].str.contains('영통구', na=False)]
Total_parking_lot_Y = Yeongtong_gu_building['총주차수'].sum() # 161155
#%% 수원시 주차장 수
All_parking_lot = (Total_parking_lot_J+Total_parking_lot_G+Total_parking_lot_P+Total_parking_lot_Y)
# 366437+8807 = 375,244

#%%

crackdown = pd.read_csv("경기도 수원시_주정차단속현황(1분기).csv")
All_count = crackdown['단속건수'].sum()# 42346
All_Money = crackdown['단속원금'].sum()# 1,862,540,000
Jangan_gu_crackdown = crackdown[crackdown['시군구명'].str.contains('장안', na=False)]
Jangan_gu_crackdown_count = Jangan_gu_crackdown['단속건수'].sum() # 4043
Jangan_gu_crackdown_Money = Jangan_gu_crackdown['단속원금'].sum() # 193,290,000

Gwonseon_gu_crackdown = crackdown[crackdown['시군구명'].str.contains('권선', na=False)]
Gwonseon_gu_crackdown_count = Gwonseon_gu_crackdown['단속건수'].sum() # 11098
Gwonseon_gu_crackdown_Money = Gwonseon_gu_crackdown['단속원금'].sum() # 494,350,000

Paldal_gu_crackdown = crackdown[crackdown['시군구명'].str.contains('팔달', na=False)]
Paldal_gu_crackdown_count = Paldal_gu_crackdown['단속건수'].sum() # 18029
Paldal_gu_crackdown_Money = Paldal_gu_crackdown['단속원금'].sum() # 724,460,000

Yeongtong_gu_crackdown = crackdown[crackdown['시군구명'].str.contains('영통', na=False)]
Yeongtong_gu_crackdown_count = Yeongtong_gu_crackdown['단속건수'].sum() # 9176
Yeongtong_gu_crackdown_Money = Yeongtong_gu_crackdown['단속원금'].sum() # 450,440,000


#%%
index_name = ["장안구",'권선구','팔달구','영통구',"총합"]
data = {"공영주차장" : [1957,2049,2306,2495,8807],
        "공영주차장수" : [13,10,14,14,51],
        "인구" : [277206,374195,194619,372801,1218821],
        "건물주차장": [66904,99211,39167,161155,366437],
        "단속건수" : [4043,11098,18029,9176,42346],
        "단속원금" : [193290000,494350000,724460000,450440000,1862540000],
        "거주자우선" : [0,0,0,0,17764]}

organize = pd.DataFrame(data,index = index_name)

organize.to_excel("주차장,인구,단속_총합.xlsx",index=True)
