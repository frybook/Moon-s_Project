# -*- coding: utf-8 -*-
import pandas as pd

# 수원시 동별 공영주차장 및 거주자우선주차구역 면수 데이터 산출하기
# 경기데이터드림 주차장 정보 현황(제공표준) : https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=1&sortColumn=&sortDirection=&infId=JHB0Z0DW2XWE342WQLR312739290&infSeq=1&searchWord=%EC%A3%BC%EC%B0%A8%EC%9E%A5
df = pd.read_csv(r"E:\workspace\python\miniproject\본프로젝트\자료조사\주차장정보현황(제공표준).csv", encoding='cp949')

# '소재지지번주소' 열의 결측치를 '소재지도로명주소' 열의 값으로 대체
df['소재지지번주소'] = df['소재지지번주소'].fillna(df['소재지도로명주소'])

# 수원시 자료만 추출하기
df = df[df['소재지지번주소'].str.contains('수원')] 

# '소재지지번주소' 열에서 앞부분 주소를 제거하고 나머지만 남기기
df['동별_구분'] = df['소재지지번주소'].str.replace(r'경기도 수원시 권선구 ', '', regex=True)
df['동별_구분'] = df['동별_구분'].str.replace(r'경기도 수원시 장안구 ', '', regex=True)
df['동별_구분'] = df['동별_구분'].str.replace(r'경기도 수원시 영통구 ', '', regex=True)
df['동별_구분'] = df['동별_구분'].str.replace(r'경기도 수원시 팔달구 ', '', regex=True)

# 필요한 열만 남기기
df = df[['주차장명', '주차장유형', '주차구획수',
        '동별_구분']]

# '동별_구분' 열의 고유값 확인 : 동만 남기기를 했는데, 일부 숫자가 붙어 있는게 있어서 확인해봄
unique_values = df['동별_구분'].unique()

# 고유값 리스트 출력
print("고유값 리스트:", unique_values)

# '동별_구분' 열을 공백으로 분리하고, 분리된 값이 2개 미만인 경우 처리
df[['word1', 'word2']] = df['동별_구분'].str.split(n=1, expand=True)

# 필요없는 열 삭제하기
df.drop(columns=['동별_구분', 'word2'], inplace=True)
df['word1']

# 여러 인덱스 동시에 변경 : 몇차례 실행해서 전처리하기
df.loc[[1007, 1008], 'word1'] = ["곡반정동", "율전동"]

df.rename(columns={'word1':'동별_구분'}, inplace=True)

# '동별_구분' 열에서 '경수대로'를 '새로운텍스트'로 치환
df['동별_구분'] = df['동별_구분'].replace('경수대로', '권선동', regex=True)

# '동별_구분' 열에서 문자열 길이가 4 이상인 데이터 필터링
filtered_df = df[df['동별_구분'].str.len() > 4]

# 결과 출력
print(filtered_df['동별_구분'])

# 동분리 잘안된 자료들 전처리
df.loc[[952, 953, 960, 963, 969, 975], '동별_구분'] = ['하광교동', '화서동', '인계동',
                                                        '하동', '영화동', '곡반정동']

df.loc[[985, 986, 989, 990, 997, 998], '동별_구분'] = ['인계동', '우만동', '인계동',
                                                        '인계동', '하동', '영통동']

df.loc[[1003, 1006], '동별_구분'] = ['이의동', '우만동']

# '동별_구분' 열을 기준으로 '주차구획수' 합계를 구하기
grouped = df.groupby('동별_구분')['주차구획수'].sum().reset_index()

grouped['주차구획수'].sum() # 9844

# '주차구획수' 내림차순 정렬
grouped = grouped.sort_values(by='주차구획수', ascending=False)

import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 그래프 생성
plt.figure(figsize=(10, 6))
bars = plt.bar(grouped['동별_구분'], grouped['주차구획수'], color='skyblue')
plt.ylabel('주차구획수')
plt.title('수원시 동별 공영주차장 구획수')
plt.xticks(rotation=90)  
plt.tight_layout()

# 막대그래프 위에 수치 표시
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 5, int(yval), ha='center', va='bottom')

# 그래프 출력
plt.show()

#%%
# 공공데이터 수원도시공사 거주자우선주차 정보 https://www.data.go.kr/data/3084454/fileData.do
df1 = pd.read_csv(r"E:\workspace\python\miniproject\본프로젝트\자료조사\경기도_수원시_거주자우선주차정보_20230823.csv", encoding='cp949')

# 거주차우선주차구획번호가 하나 하나의 주차면수를 의미하는 것임 : 샘플확인용 데이터 추출
# df1_suwon1 = df1[df1['거주자우선주차구획번호'].str.contains('56-94')]

# 필요한 열만 남기기
df1 = df1[['거주자우선주차구획위도',
 '거주자우선주차구획경도',
 '소재지지번주소']]

# '소재지지번주소' 열에서 동만 남기기
df1['동별_구분'] = df1['소재지지번주소'].str.split(' ').str[3]
df1.drop(columns='소재지지번주소', inplace=True)

# '동별_구분' 열의 고유값 확인 : 동만 남기기를 했는데, 일부 숫자가 붙어 있는게 있어서 확인해봄
unique_values = df1['동별_구분'].unique()

# 고유값 리스트 출력
print("고유값 리스트:", unique_values)

# '동별_구분' 열에서 문자열 길이가 4 이상인 데이터 필터링
filtered_df = df1[df1['동별_구분'].str.len() > 4]

# 결과 출력
print(filtered_df['동별_구분'])

# 여러 인덱스 동시에 변경 : 몇차례 실행해서 전처리하기
df1.loc[[3573, 3574, 3575, 3576,3577], '동별_구분'] = ["구운동", "구운동", "구운동", "구운동", "구운동"]
df1.loc[[3578, 3579, 3580, 4279, 4853], '동별_구분'] = ["구운동", "구운동", "구운동", "권선동", "서둔동"]
df1.loc[[6722, 6723, 6724, 6725, 6726], '동별_구분'] = ["세류동", "세류동", "세류동", "세류동", "세류동"]
df1.loc[[6727, 6728, 6729, 6730, 6731], '동별_구분'] = ["세류동", "세류동", "세류동", "세류동", "세류동"]
df1.loc[[8954, 9099], '동별_구분'] = ["매탄동", "신동"]

df1['주차면수'] = 1

df1['주차면수'].sum()   # 17632

# df에서 '동별_구분'별로 '주차구획수' 합산
df_sum = df.groupby('동별_구분')['주차구획수'].sum().reset_index()
df1_sum = df1.groupby('동별_구분')['주차면수'].sum().reset_index()

# df와 df1_sum을 병합
merged_df = pd.merge(df_sum, df1_sum, on='동별_구분', how='outer', suffixes=('_공영', '_거주자'))

# NaN 값을 0으로 대체
merged_df['주차구획수_공영'] = merged_df['주차구획수'].fillna(0)
merged_df['주차면수_거주자'] = merged_df['주차면수'].fillna(0)

# 총 주차면수 계산
merged_df['총_주차면수'] = merged_df['주차구획수_공영'] + merged_df['주차면수_거주자']

# 각 주차장 유형별 합계 확인
print(f"공영 주차장 총 주차면수: {merged_df['주차구획수_공영'].sum()}")
print(f"거주자 우선 주차 총 주차면수: {merged_df['주차면수_거주자'].sum()}")
# 결과 확인
merged_df['총_주차면수'].sum()   # 27476.0

#%%
# 건축물대장상 주차면수와 합치기
const = pd.read_csv(r"E:\workspace\python\miniproject\본프로젝트\자료조사\건축물대장상주차면수.csv")

const.rename(columns={'동이름':'동별_구분'}, inplace=True)

const.info()
# Data columns (total 3 columns):
#  #   Column      Non-Null Count  Dtype 
# ---  ------      --------------  ----- 
#  0   Unnamed: 0  54 non-null     int64 
#  1   동별_구분       54 non-null     object
#  2   총주차수        54 non-null     int64 
# dtypes: int64(2), object(1)
# memory usage: 1.4+ KB

const['총주차수'].sum()  # 376154

# mergedf와 const를 병합
final_df = pd.merge(merged_df, const[['동별_구분', '총주차수']], on='동별_구분', how='outer')

# NaN 값을 0으로 대체
final_df['주차구획수_공영'] = final_df['주차구획수_공영'].fillna(0)
final_df['주차면수_거주자'] = final_df['주차면수_거주자'].fillna(0)
final_df['총주차수'] = final_df['총주차수'].fillna(0)

final_df['주차구획수_공영'].sum() # 9844
final_df['주차면수_거주자'].sum() # 17632
final_df['총주차수'].sum() # 376154

# 최종 총 주차면수 계산
final_df['최종_총_주차면수'] = final_df['주차구획수_공영'] + final_df['주차면수_거주자'] + final_df['총주차수']

# 결과 확인
print(final_df)

# 각 주차장 유형별 합계 확인
print(f"공영 주차장 총 주차면수: {final_df['주차구획수_공영'].sum()}")
print(f"거주자 우선 주차 총 주차면수: {final_df['주차면수_거주자'].sum()}")
print(f"건축물대장상 총 주차면수: {final_df['총주차수'].sum()}")
print(f"최종 총 주차면수: {final_df['최종_총_주차면수'].sum()}")

# 각 데이터프레임의 원래 합계 확인
print(f"\n원래 데이터의 합계:")
print(f"mergedf 총 주차면수: {merged_df['총_주차면수'].sum()}")
print(f"const 총 주차수: {const['총주차수'].sum()}")
print(f"예상되는 최종 총 주차면수: {merged_df['총_주차면수'].sum() + const['총주차수'].sum()}")

# '최종_총_주차면수'를 기준으로 내림차순 정렬
# final_df_sorted = final_df.sort_values(by='최종_총_주차면수', ascending=False)

# 한글 폰트 설정
from matplotlib import font_manager, rc
font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# '최종_총_주차면수'를 기준으로 내림차순 정렬하고 상위 20개만 선택
final_df_sorted = final_df.sort_values(by='최종_총_주차면수', ascending=False).head(20)

# 그래프 생성
plt.figure(figsize=(15, 8))
bars = plt.bar(final_df_sorted['동별_구분'], final_df_sorted['최종_총_주차면수'], color='skyblue')
plt.ylabel('총 주차면수')
plt.title('수원시 동별 총 주차면수 (상위 20개 동)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# 막대그래프 위에 수치 표시 (180도 회전)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), 
             ha='center', va='top', rotation=180)

# y축 limit 설정 (수치가 잘 보이도록 여유 공간 추가)
plt.ylim(0, max(final_df_sorted['최종_총_주차면수']) * 1.1)

# 그래프 출력
plt.savefig('수원시주차장현황.png', dpi=300)
plt.show()


#%%
# 공영주차장만 별도 표시

# '주차구획수_공영'을 기준으로 내림차순 정렬하고 상위 20개만 선택
public_parking_top20 = final_df.sort_values(by='주차구획수_공영', ascending=False).head(20)

# 그래프 생성
plt.figure(figsize=(15, 8))
bars = plt.bar(public_parking_top20['동별_구분'], public_parking_top20['주차구획수_공영'], color='lightgreen')
plt.ylabel('공영주차장 주차구획수')
plt.title('수원시 동별 공영주차장 주차구획수 (상위 20개 동)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# 막대그래프 위에 수치 표시
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), 
             ha='center', va='bottom', rotation=0)

# y축 limit 설정 (수치가 잘 보이도록 여유 공간 추가)
plt.ylim(0, max(public_parking_top20['주차구획수_공영']) * 1.1)

# 그래프 출력
plt.savefig('공영주차장 현황.png', dpi=300)
plt.show()