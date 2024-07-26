# -*- coding: utf-8 -*-
import pandas as pd

# 출처 : 경기데이터드림
# https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=1&sortColumn=&sortDirection=&infId=SVTOOYGZR861O3HGNCET34183944&infSeq=1&searchWord=%EA%B1%B4%EC%B6%95%EB%AC%BC%EB%8C%80%EC%9E%A5
# 파일경로는 바꿔야 함
df = pd.read_csv(r"C:\Users\goido\Downloads\경기부동산포털_건물_총괄표제부.csv", encoding='euc-kr')

list(df)

# 필요없는 열 삭제
df.drop(['토지고유번호', '건물번호'], axis=1, inplace=True)

df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 129701 entries, 0 to 129700
# Data columns (total 15 columns):
#  #   Column  Non-Null Count   Dtype  
# ---  ------  --------------   -----  
#  0   토지소재지   129698 non-null  object 
#  1   건물명     23877 non-null   object 
#  2   외필지수    129701 non-null  int64  
#  3   대지면적    129701 non-null  float64
#  4   건축면적    129701 non-null  float64
#  5   건폐율     129701 non-null  float64
#  6   연면적     129701 non-null  float64
#  7   용적율     129701 non-null  float64
#  8   주용도코드   127830 non-null  object 
#  9   주건축물수   129701 non-null  int64  
#  10  부속건축물수  129701 non-null  int64  
#  11  총주차수    129701 non-null  int64  
#  12  허가일     68255 non-null   object 
#  13  착공일     65032 non-null   object 
#  14  사용승인일   74917 non-null   object 
# dtypes: float64(5), int64(4), object(6)
# memory usage: 14.8+ MB

# 계산이 가능하도록 정수타입으로 변환
df[['대지면적', '건축면적', '건폐율', '연면적', '용적율', '총주차수']].astype(int)