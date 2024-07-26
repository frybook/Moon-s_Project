# -*- coding: utf-8 -*-
import pandas as pd

# 경기도 수원시_주정차단속현황 : 2023년 1년 기준
# https://www.data.go.kr/data/15063802/fileData.do#layer_data_infomation
df= pd.read_csv("경기도_수원시_주정차단속현황_20240122.CSV", encoding='euc-kr')

list(df)
# Out[56]: ['시군구명', '단속구분', '단속년월', '단속동', '단속건수', '단속원금']

# '단속건수'가 많은 순서대로 정렬
sorted_df = df.sort_values(by='단속건수', ascending=False)

# 상위 5개 '단속동' 확인
top_5_dansok_dong = sorted_df.head(5)[['단속동', '단속건수']]

print(top_5_dansok_dong)
#        단속동 단속건수
# 57002  영통동   99
# 44534  매탄동   99
# 5014   화서동   99
# 13873   지동   99
# 16597  망포동   99

# 1등이 안나와서 2022년도 자료까지 포함해서 다시 확인하기

df1= pd.read_csv("경기도_수원시_주정차단속현황_20221227.csv", encoding='euc-kr')

pdf = pd.concat([df, df1])

# '단속건수'가 많은 순서대로 정렬
sorted_df = pdf.sort_values(by='단속건수', ascending=False)

# 상위 5개 '단속동' 확인
top_5_dansok_dong = sorted_df.head(5)[['단속동', '단속건수']]

print(top_5_dansok_dong)

# 그래도 같이 같아서 자료형태 확인해 보기

pdf.info()
# <class 'pandas.core.frame.DataFrame'>
# Index: 104721 entries, 0 to 44563
# Data columns (total 6 columns):
#  #   Column  Non-Null Count   Dtype 
# ---  ------  --------------   ----- 
#  0   시군구명    104721 non-null  object
#  1   단속구분    104721 non-null  object
#  2   단속년월    104721 non-null  object
#  3   단속동     104721 non-null  object
#  4   단속건수    104721 non-null  object
#  5   단속원금    104721 non-null  object
# dtypes: object(6)
# memory usage: 5.6+ MB

# 단속건수가 계산할 수 없는 형태라 문제가 생김. 자료형 바꾸기
# 천 단위 구분자 제거 및 정수형으로 변환
pdf['단속건수'] = pdf['단속건수'].str.replace(',', '').astype(int)

# '단속동'별 '단속건수' 합계 계산
grouped = pdf.groupby('단속동')['단속건수'].sum().reset_index()

# '단속건수'가 많은 순서대로 정렬
sorted_grouped = grouped.sort_values(by='단속건수', ascending=False)

print(sorted_grouped)
#      단속동    단속건수
# 62   인계동  139909
# 31   매탄동   56533
# 50   영통동   54190
# 61   이의동   44415
# 56   원천동   37600

## 결론 : 수원에서는 인계동이 주정차 위반 단속이 가장 많이 발생하고 있음.


