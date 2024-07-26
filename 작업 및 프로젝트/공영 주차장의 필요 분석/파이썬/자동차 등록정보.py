import pandas as pd


# 수원시 자동차 수
df = pd.read_excel("수원시자동차등록수.xlsx")
Suwon_city_Car_total = df['총계'].sum() # 561679
df.loc[len(df)] = [None] * (df.shape[1] - 1) + [Suwon_city_Car_total]
Suwon_city = df['총계']


# 
Suwon_City_parking_spot = pd.read_excel("주차장,인구,단속_총합.xlsx")
Suwon_City_parking_spot['총계'] = Suwon_city


Suwon_City_parking_spot.to_excel("주차장,인구,단속,자동차등록,총합.xlsx",index=True)


