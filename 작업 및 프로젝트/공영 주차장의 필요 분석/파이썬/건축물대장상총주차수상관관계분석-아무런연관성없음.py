# -*- coding: utf-8 -*-
import pandas as pd

# 출처 : 경기데이터드림
# https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=1&sortColumn=&sortDirection=&infId=SVTOOYGZR861O3HGNCET34183944&infSeq=1&searchWord=%EA%B1%B4%EC%B6%95%EB%AC%BC%EB%8C%80%EC%9E%A5
# 파일경로는 바꿔야 함
df = pd.read_csv(r"C:\Users\Charlie\Downloads\경기부동산포털_건물_총괄표제부.csv", encoding='euc-kr')

list(df)

# 필요한 열만 선택함으로써 필요없는 열 삭제
selected_df = df[['토지소재지',
  '건물명',
  '대지면적',
  '건축면적',
  '건폐율',
  '연면적',
  '용적율',
  '주건축물수',
  '부속건축물수',
  '총주차수']]

df = selected_df

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

## 데이터 분석하기
# 기본 통계 확인: 데이터의 전반적인 특성을 파악합니다.
# 상관관계 분석: 총주차수와 다른 변수들 간의 관계를 확인합니다.
# 연면적과 총주차수의 관계: 건물 크기와 주차 공간의 관계를 시각화합니다.
# 건물 용도별 평균 총주차수: 주거시설과 비주거시설의 주차 공간 차이를 비교합니다.
# 주차수/연면적 비율: 건물 크기 대비 주차 공간의 효율성을 분석합니다.
# 용적률과 총주차수의 관계: 건물의 밀도와 주차 공간의 관계를 확인합니다.
# 총주차수가 0인 건물 분석: 주차 공간이 없는 건물의 특성을 파악합니다.
# 대지면적 대비 총주차수 비율: 토지 이용 효율성을 분석합니다.
# 주건축물수와 총주차수의 관계: 건물 수와 주차 공간의 관계를 확인합니다.
# 건물 크기나 용도에 따른 주차 공간 확보 패턴, 토지 이용 효율성, 주차 공간이
# 부족한 건물의 특성 등을 파악할 수 있음

import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# 기본 통계 확인
print(df.describe())
#                대지면적          건축면적  ...         부속건축물수           총주차수
# count  1.297010e+05  1.297010e+05  ...  129701.000000  129701.000000
# mean   7.150828e+03  1.434120e+03  ...       0.415132      34.712963
# std    9.092204e+04  2.408397e+04  ...       2.408561     205.065032
# min    0.000000e+00  0.000000e+00  ...       0.000000       0.000000
# 25%    6.580000e+02  2.302500e+02  ...       0.000000       0.000000
# 50%    1.395000e+03  4.572800e+02  ...       0.000000       2.000000
# 75%    3.257000e+03  9.986400e+02  ...       0.000000       6.000000
# max    1.515954e+07  4.368936e+06  ...     318.000000   19127.000000
# [8 rows x 8 columns]

# 총주차수와 다른 변수들 간의 상관관계 분석
correlation_matrix = df[['대지면적', '건축면적', '건폐율', '연면적', '용적율', '주건축물수', '부속건축물수', '총주차수']].corr()
print("\n상관관계 매트릭스:")
print(correlation_matrix['총주차수'].sort_values(ascending=False))
상관관계 매트릭스:
총주차수      1.000000
부속건축물수    0.540637
대지면적      0.131481
건축면적      0.100192
연면적       0.025400
건폐율       0.010081
주건축물수     0.006652
용적율      -0.000127
Name: 총주차수, dtype: float64

# 총주차수와 연면적의 산점도
plt.figure(figsize=(10, 6))
plt.scatter(df['연면적'], df['총주차수'])
plt.title('연면적과 총주차수의 관계')
plt.xlabel('연면적')
plt.ylabel('총주차수')
plt.show()

# 건물 용도별 평균 총주차수
df['건물용도'] = df['건물명'].apply(lambda x: '주거시설' if '아파트' in str(x) else '비주거시설')
avg_parking_by_usage = df.groupby('건물용도')['총주차수'].mean()
print("\n건물 용도별 평균 총주차수:")
print(avg_parking_by_usage)

# 총주차수 대 연면적 비율 계산
df['주차수_연면적_비율'] = df['총주차수'] / df['연면적']
print("\n주차수/연면적 비율 통계:")
print(df['주차수_연면적_비율'].describe())

# 용적률과 총주차수의 관계
plt.figure(figsize=(10, 6))
plt.scatter(df['용적율'], df['총주차수'])
plt.title('용적률과 총주차수의 관계')
plt.xlabel('용적률')
plt.ylabel('총주차수')
plt.show()

# 총주차수가 0인 건물 분석
zero_parking = df[df['총주차수'] == 0]
print("\n총주차수가 0인 건물 수:", len(zero_parking))
print("총주차수가 0인 건물의 평균 대지면적:", zero_parking['대지면적'].mean())

# 대지면적 대비 총주차수 비율
df['주차수_대지면적_비율'] = df['총주차수'] / df['대지면적']
print("\n대지면적 대비 총주차수 비율 통계:")
print(df['주차수_대지면적_비율'].describe())

# 주건축물수와 총주차수의 관계
plt.figure(figsize=(10, 6))
plt.scatter(df['주건축물수'], df['총주차수'])
plt.title('주건축물수와 총주차수의 관계')
plt.xlabel('주건축물수')
plt.ylabel('총주차수')
plt.show()


#%%

# 건물 용도 분류 함수
def classify_building(name):
    if '아파트' in name:
        return '공동주택'
    elif '학교' in name:
        return '학교'
    elif '운수' in name:
        return '운수'
    else:
        return '기타'

# 건물 용도 분류
df['건물용도'] = df['건물명'].apply(classify_building)

# 주차 기준 충족 여부 확인 함수
def check_parking_standard(row):
    if row['건물용도'] == '공동주택':
        return row['총주차수'] >= (row['연면적'] // 75)  # 75m^2당 1대
    elif row['건물용도'] == '학교':
        return row['총주차수'] >= (row['연면적'] // 200)  # 200m^2당 1대
    elif row['건물용도'] == '운수':
        return row['총주차수'] >= (row['연면적'] // 100)  # 100m^2당 1대
    else:
        return row['총주차수'] >= (row['연면적'] // 150)  # 기타 용도는 150m^2당 1대로 가정

# 주차 기준 충족 여부 확인
df['주차기준충족'] = df.apply(check_parking_standard, axis=1)

# 용도별 주차 기준 충족률 계산
compliance_rate = df.groupby('건물용도')['주차기준충족'].mean()

# 결과 출력
print("용도별 주차 기준 충족률:")
print(compliance_rate)

# 용도별 평균 주차 비율 계산 (실제 주차수 / 기준 주차수)
def calculate_parking_ratio(row):
    if row['건물용도'] == '공동주택':
        return row['총주차수'] / (row['연면적'] // 75) if row['연면적'] > 0 else 0
    elif row['건물용도'] == '학교':
        return row['총주차수'] / (row['연면적'] // 200) if row['연면적'] > 0 else 0
    elif row['건물용도'] == '운수':
        return row['총주차수'] / (row['연면적'] // 100) if row['연면적'] > 0 else 0
    else:
        return row['총주차수'] / (row['연면적'] // 150) if row['연면적'] > 0 else 0

df['주차비율'] = df.apply(calculate_parking_ratio, axis=1)

average_ratio = df.groupby('건물용도')['주차비율'].mean()

print("\n용도별 평균 주차 비율 (실제/기준):")
print(average_ratio)

# 시각화: 용도별 주차 기준 충족률
plt.figure(figsize=(10, 6))
compliance_rate.plot(kind='bar')
plt.title('용도별 주차 기준 충족률')
plt.ylabel('충족률')
plt.xlabel('건물 용도')
plt.show()

# 시각화: 용도별 평균 주차 비율
plt.figure(figsize=(10, 6))
average_ratio.plot(kind='bar')
plt.title('용도별 평균 주차 비율 (실제/기준)')
plt.ylabel('주차 비율')
plt.xlabel('건물 용도')
plt.show()

#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV 파일 로드
df = pd.read_csv('parklot.csv', encoding='utf-8')

# 날짜 컬럼을 datetime 형식으로 변환
date_columns = ['허가일', '착공일', '사용승인일']
for col in date_columns:
    df[col] = pd.to_datetime(df[col], format='%Y%m%d', errors='coerce')

# 주용도코드를 문자열로 변환 (앞의 0 유지를 위해)
df['주용도코드'] = df['주용도코드'].astype(str).str.zfill(5)

# 기본 통계 확인
print(df.describe())

# 주용도코드별 외필지수 평균 계산
usage_avg_parklots = df.groupby('주용도코드')['외필지수'].mean().sort_values(ascending=False)
print("\n주용도코드별 평균 외필지수:")
print(usage_avg_parklots)

# 연도별 건축물 수 추이
df['사용승인연도'] = df['사용승인일'].dt.year
yearly_buildings = df['사용승인연도'].value_counts().sort_index()

## 시각화하기
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한글 폰트를 설정
plt.rcParams['font.family'] = 'Malgun Gothic'

# 그래프에서 마이너스 폰트가 깨지는 문제를 해결
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(12, 6))
yearly_buildings.plot(kind='bar')
plt.title('연도별 사용승인 건축물 수')
plt.xlabel('년도')
plt.ylabel('건축물 수')
plt.show()

# 주용도코드별 외필지수 분포 (박스플롯)
plt.figure(figsize=(12, 6))
sns.boxplot(x='주용도코드', y='외필지수', data=df)
plt.title('주용도코드별 외필지수 분포')
plt.xticks(rotation=90)
plt.show()

# 허가일부터 사용승인일까지의 기간 계산
df['건설기간'] = (df['사용승인일'] - df['허가일']).dt.days
print("\n평균 건설 기간 (일):")
print(df['건설기간'].mean())

# 건설기간과 외필지수의 상관관계
correlation = df['건설기간'].corr(df['외필지수'])
print(f"\n건설기간과 외필지수의 상관계수: {correlation}")

# 건설기간과 외필지수의 산점도
plt.figure(figsize=(10, 6))
plt.scatter(df['건설기간'], df['외필지수'])
plt.title('건설기간과 외필지수의 관계')
plt.xlabel('건설기간 (일)')
plt.ylabel('외필지수')
plt.show()