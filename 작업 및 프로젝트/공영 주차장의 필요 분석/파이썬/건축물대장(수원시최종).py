# -*- coding: utf-8 -*-
import pandas as pd

# http://www.geobigdata.go.kr/portal/case/standardView.do?proj_seq=34
# 수원시 건축물대장 총괄표제부 자료 : 건축데이터개발 사이트에서 가져옴
# https://open.eais.go.kr/opnsvc/opnSvcInqireView.do?viewType=1&searchCondition=01&opnSvcSn=19&searchKeyword=%EA%B1%B4%EC%B6%95%EB%8D%B0%EC%9D%B4%ED%84%B0
gsdf = pd.read_excel(r"C:\Users\Charlie\Downloads\총괄표제부 조회.xlsx", header=None)
ytdf = pd.read_excel(r"C:\Users\Charlie\Downloads\총괄표제부 조회 (1).xlsx", header=None)
pddf = pd.read_excel(r"C:\Users\Charlie\Downloads\총괄표제부 조회 (2).xlsx", header=None)
jadf = pd.read_excel(r"C:\Users\Charlie\Downloads\총괄표제부 조회 (3).xlsx", header=None)

# 데이터 전처리
## 권선구 전인덱스 4의 데이터를 열 이름으로 설정
gsdf.columns = gsdf.iloc[4]
ytdf.columns = ytdf.iloc[4]
jadf.columns = jadf.iloc[4]
pddf.columns = pddf.iloc[4]

# 인덱스 4와 그 이전의 행들을 제거
gsdf = gsdf.drop(index=list(range(5)))
ytdf = ytdf.drop(index=list(range(5)))
jadf = jadf.drop(index=list(range(5)))
pddf = pddf.drop(index=list(range(5)))

# 인덱스를 리셋
gsdf = gsdf.reset_index(drop=True)
ytdf = ytdf.reset_index(drop=True)
jadf = jadf.reset_index(drop=True)
pddf = pddf.reset_index(drop=True)

jadf.isnull().sum()

# 필요없는 열 삭제하기
gsdf.drop(['대지구분코드', '번', '지', '순번', '허가번호년', '허가번호기관코드', '허가번호기관코드명',
 '허가번호구분코드', '허가번호구분코드명', '호수(호)', '에너지효율등급',
 '에너지절감율', 'EPI점수', '친환경건축물등급', '친환경건축물인증점수',
 '지능형건축물등급', '지능형건축물인증점수', '생성일자', '특수지명', '블록', '로트', '새주소도로코드', '새주소법정동코드',
            '새주소지상지하코드', '새주소본번', '새주소부번'], axis=1, inplace=True)
ytdf.drop(['대지구분코드', '번', '지', '순번', '허가번호년', '허가번호기관코드', '허가번호기관코드명',
 '허가번호구분코드', '허가번호구분코드명', '호수(호)', '에너지효율등급',
 '에너지절감율', 'EPI점수', '친환경건축물등급', '친환경건축물인증점수',
 '지능형건축물등급', '지능형건축물인증점수', '생성일자', '특수지명', '블록', '로트', '새주소도로코드', '새주소법정동코드',
            '새주소지상지하코드', '새주소본번', '새주소부번'], axis=1, inplace=True)
jadf.drop(['대지구분코드', '번', '지', '순번', '허가번호년', '허가번호기관코드', '허가번호기관코드명',
 '허가번호구분코드', '허가번호구분코드명', '호수(호)', '에너지효율등급',
 '에너지절감율', 'EPI점수', '친환경건축물등급', '친환경건축물인증점수',
 '지능형건축물등급', '지능형건축물인증점수', '생성일자', '특수지명', '블록', '로트', '새주소도로코드', '새주소법정동코드',
            '새주소지상지하코드', '새주소본번', '새주소부번'], axis=1, inplace=True)
pddf.drop(['대지구분코드', '번', '지', '순번', '허가번호년', '허가번호기관코드', '허가번호기관코드명',
 '허가번호구분코드', '허가번호구분코드명', '호수(호)', '에너지효율등급',
 '에너지절감율', 'EPI점수', '친환경건축물등급', '친환경건축물인증점수',
 '지능형건축물등급', '지능형건축물인증점수', '생성일자', '특수지명', '블록', '로트', '새주소도로코드', '새주소법정동코드',
            '새주소지상지하코드', '새주소본번', '새주소부번'], axis=1, inplace=True)

gsdf.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1136 entries, 0 to 1135
# Data columns (total 39 columns):
#  #   Column       Non-Null Count  Dtype 
# ---  ------       --------------  ----- 
#  0   대지위치         1136 non-null   object
#  1   시군구코드        1136 non-null   object
#  2   법정동코드        1136 non-null   object
#  3   관리건축물대장PK    1136 non-null   object
#  4   대장구분코드       1136 non-null   object
#  5   대장구분코드명      1136 non-null   object
#  6   대장종류코드       1136 non-null   object
#  7   대장종류코드명      1136 non-null   object
#  8   신구대장구분코드     1135 non-null   object
#  9   신구대장구분코드명    1135 non-null   object
#  10  도로명대지위치      1136 non-null   object
#  11  건물명          399 non-null    object
#  12  외필지수         1136 non-null   object
#  13  대지면적(㎡)      1136 non-null   object
#  14  건축면적(㎡)      1136 non-null   object
#  15  건폐율(%)       1136 non-null   object
#  16  연면적(㎡)       1136 non-null   object
#  17  용적률산정연면적(㎡)  1136 non-null   object
#  18  용적률(%)       1136 non-null   object
#  19  주용도코드        1088 non-null   object
#  20  주용도코드명       1088 non-null   object
#  21  기타용도         1064 non-null   object
#  22  세대수(세대)      1136 non-null   object
#  23  가구수(가구)      1136 non-null   object
#  24  주건축물수        1136 non-null   object
#  25  부속건축물수       1136 non-null   object
#  26  부속건축물면적(㎡)   1136 non-null   object
#  27  총주차수         1136 non-null   object
#  28  옥내기계식대수(대)   1136 non-null   object
#  29  옥내기계식면적(㎡)   1136 non-null   object
#  30  옥외기계식대수(대)   1136 non-null   object
#  31  옥외기계식면적(㎡)   1136 non-null   object
#  32  옥내자주식대수(대)   1136 non-null   object
#  33  옥내자주식면적(㎡)   1136 non-null   object
#  34  옥외자주식대수(대)   1136 non-null   object
#  35  옥외자주식면적(㎡)   1136 non-null   object
#  36  허가일          352 non-null    object
#  37  착공일          348 non-null    object
#  38  사용승인일        353 non-null    object
# dtypes: object(39)
# memory usage: 346.3+ KB

# 수원시만 따로 모으기
suwonbldg = pd.concat([jadf, pddf, ytdf, gsdf])

df = suwonbldg

# 주소 단순화하기
df['대지위치'] = df['대지위치'].str.replace('경기도 ', '').str.replace('수원시 ', '')

list(df)

# 필요한 열만 남기기
df = df[['대지위치',
 '법정동코드',
 '대장구분코드명',
 '건물명',
 '외필지수',
 '대지면적(㎡)',
 '건축면적(㎡)',
 '건폐율(%)',
 '연면적(㎡)',
 '용적률산정연면적(㎡)',
 '용적률(%)',
 '주용도코드',
 '주용도코드명',
 '기타용도',
 '세대수(세대)',
 '가구수(가구)',
 '주건축물수',
 '부속건축물수',
 '부속건축물면적(㎡)',
 '총주차수',
 '허가일',
 '착공일',
 '사용승인일']]

df.info() # 다 object형임

# 계산이 가능하도록 타입으로 변환
df[[ '외필지수',
 '대지면적(㎡)',
 '건축면적(㎡)',
 '건폐율(%)',
 '연면적(㎡)',
 '용적률산정연면적(㎡)',
 '용적률(%)',
 '주건축물수',
 '부속건축물수',
 '부속건축물면적(㎡)']].astype(float)
df[['세대수(세대)',
 '가구수(가구)',
 '주건축물수',
 '부속건축물수',
 '총주차수']].astype(int)
df[['주용도코드']].astype(str)

df.to_csv('수원시건축물대장.csv')
