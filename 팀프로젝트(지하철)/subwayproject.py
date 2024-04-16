# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CSV 파일 경로 설정
file_path = "E:/workspace/python/miniproject0408/subway/데이터 정보/서울시 지하철 호선별 역별 시간대별 승하차 인원 정보.csv"

# CSV 파일을 데이터프레임으로 변환
subway_people = pd.read_csv(file_path, encoding='euc-kr')

# 불필요한 작업일자 컬럼 제거
subway_people = subway_people.drop(columns=['작업일자'])

# 2023.01 그 전 데이터는 제외
for i in subway_people.index:
    if int(subway_people.loc[i, ['사용월']]) == 202301:
        break

subway_people = subway_people.loc[:9246, :]

# 승차인원만 추출
in_df = subway_people.columns.tolist()[:3]
for a in subway_people.columns.tolist():
    if a.find('승차') != -1:
        in_df.append(a)
in_df1 = subway_people[in_df]

# 폰트 설치하기
import matplotlib.font_manager as fm
from collections import Counter
font_files = fm.findSystemFonts(fontpaths=['C:/Users/Charlie/AppData/Local/Microsoft/Windows/Fonts/'])
for fpath in font_files:
    fm.fontManager.addfont(fpath)
plt.rcParams['font.family'] = 'NanumGothic'

plt.rcParams['font.size'] = 11

# # 승차인원만 합계 구하기
in_df1['승차합계'] = in_df1[[column for column in in_df1.columns if '승차인원' in column]].sum(axis=1)
    
# 상위 15개 지하철역 추출
top_15_stations = in_df1.groupby('지하철역')['승차합계'].sum().nlargest(15)

# 막대 그래프 그리기
ax = top_15_stations.plot(kind='bar')

# 각 막대 위에 값 표시 (단위: 백만 명)
for i in ax.patches:
    ax.text(i.get_x() + i.get_width() / 2, i.get_height(), f"{i.get_height() / 1000000:.1f}", ha='center', va='bottom')

# 축 레이블 추가
plt.ylabel('승차인원합계(백만 명)')

# 제목 추가
plt.title('서울 지하철 승차인원 top 15(23.1~24.3 기준)')

# 그래프 표시
plt.show()


########################################
밑에 부분은 연습용임
#######################################



## 지하철역별 승차인원 막대그래프 그리기 성공
# in_df1.groupby('지하철역')['승차합계'].sum().sort_values().plot(kind='bar')


## '승차' 문자열을 포함하는 열에 대해 승차합계 구하기
# 승차열 = in_df1.loc[:, in_df1.columns.str.contains('승차')]
# in_df1['승차합계1'] = 승차열.sum(axis=1)

# 승차인원 기준 내림차순 정렬하기
in_df1_sorted = in_df1.sort_values(by='승차합계1', ascending=False)

# 열 합계 구하기
column_sum = in_df1.iloc[:, 3:].sum(axis=0)

# 새로운 행 추가
in_df1.loc['합계'] = column_sum

print(in_df1)


## 특정 열에서 열까지 열합계 구하기(예제1)
data = {'A': [1, 2, 3],
        'B-승차': [4, 5, 6],
        'C-승차': [7, 8, 9]}
df = pd.DataFrame(data)
# print(df)
#    A  B-승차  C-승차
# 0  1     4     7
# 1  2     5     8
# 2  3     6     9

# 열 합계 구하기
column_sum = df.iloc[:, :].sum(axis=0)

# 새로운 행 추가
df.loc['합계'] = column_sum
print(df)
#       A  B-승차  C-승차
# 0   1.0   4.0   7.0
# 1   2.0   5.0   8.0
# 2   3.0   6.0   9.0
# 합계  NaN  15.0  24.0


## 특정 열에서 열까지 열합계 구하기(예제1)
data = {'A': ['1호선', '2호선', '3호선'],
        'A-승차': [1, 2, 3],
        'B-승차': [4, 5, 6],
        'C-승차': [7, 8, 9]}
df = pd.DataFrame(data)
print(df)
#      A  A-승차  B-승차  C-승차
# 0  1호선     1     4     7
# 1  2호선     2     5     8
# 2  3호선     3     6     9

# 열 합계 구하기
column_sum = df.iloc[:, 1:].sum(axis=0)

# 새로운 행 추가
df.loc['합계'] = column_sum
print(df)
#       A  A-승차  B-승차  C-승차
# 0   1호선   1.0   4.0   7.0
# 1   2호선   2.0   5.0   8.0
# 2   3호선   3.0   6.0   9.0
# 합계  NaN   6.0  15.0  24.0


## '승차' 문자열을 가지고 있는 열에 대해 합계를 구하여 새로운 열 '승차합계'를 만듦(방법1)

df['승차합계'] = df[[column for column in df.columns if '승차' in column]].sum(axis=1)

print("결과값:")
print(df)
# 결과값:
#       A  A-승차  B-승차  C-승차  승차합계
# 0   1호선   1.0   4.0   7.0  12.0
# 1   2호선   2.0   5.0   8.0  15.0
# 2   3호선   3.0   6.0   9.0  18.0
# 합계  NaN   6.0  15.0  24.0  45.0

## '승차' 문자열을 가지고 있는 열에 대해 합계 구하기(방법2)
# 데이터프레임 생성
data = {'A': ['1호선', '2호선', '3호선'],
        'A-승차': [1, 2, 3],
        'B-승차': [4, 5, 6],
        'C-승차': [7, 8, 9]}
df = pd.DataFrame(data)

# '승차합계' 열 추가
df['승차합계'] = df[['A-승차', 'B-승차', 'C-승차']].sum(axis=1)

# 결과 출력
print(df)

## '승차' 문자열을 가지고 있는 열에 대해 합계 구하기(방법3)
# 데이터프레임 생성
data = {'A': ['1호선', '2호선', '3호선'],
        'A-승차': [1, 2, 3],
        'B-승차': [4, 5, 6],
        'C-승차': [7, 8, 9]}
df = pd.DataFrame(data)

# '승차' 문자열을 포함하는 열에 대해 승차합계 구하기
승차열 = df.loc[:, df.columns.str.contains('승차')]
df['승차합계'] = 승차열.sum(axis=1)

# 결과 출력
print(df)


