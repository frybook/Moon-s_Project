# -*- coding: utf-8 -*-
# 4개동 인구비교 막대그래프 그리기 성공
import pandas as pd
import matplotlib.pyplot as plt

# https://jumin.mois.go.kr/ : 법정동별 주민등록 인구통계
df = pd.read_csv("202405_202405_연령별인구현황_월간.csv", encoding='euc-kr')

columns = df.columns.tolist()

# 삭제할 열 인덱스 범위 지정 
start_idx = 1
end_idx = 16
columns_to_drop = columns[start_idx:end_idx]

# 열 삭제
df = df.drop(columns=columns_to_drop)

# 삭제하는 열 직접 지정하기
df.drop(['2024년05월_여_총인구수', '2024년05월_여_연령구간인구수'], axis=1, inplace=True)

# 열 이름 변경
df = df.rename(columns={
    '법정구역':'법정구역',
    '2024년05월_남_0~9세':'남0~9세',
    '2024년05월_남_10~19세':'남10대',
    '2024년05월_남_20~29세':'남20대',
    '2024년05월_남_30~39세':'남30대',
    '2024년05월_남_40~49세':'남40대',
    '2024년05월_남_50~59세':'남50대',
    '2024년05월_남_60~69세':'남60대',
    '2024년05월_남_70~79세':'남70대',
    '2024년05월_남_80~89세':'남80대',
    '2024년05월_남_90~99세':'남90대',
    '2024년05월_남_100세 이상':'남100세이상',
    '2024년05월_여_0~9세':'여0~9세',
    '2024년05월_여_10~19세':'여10대',
    '2024년05월_여_20~29세':'여20대',
    '2024년05월_여_30~39세':'여30대',
    '2024년05월_여_40~49세':'여40대',
    '2024년05월_여_50~59세':'여50대',
    '2024년05월_여_60~69세':'여60대',
    '2024년05월_여_70~79세':'여70대',
    '2024년05월_여_80~89세':'여80대',
    '2024년05월_여_90~99세':'여90대',
    '2024년05월_여_100세 이상':'여100세이상'
})

# 남자와 여자 인구수를 합한 새로운 열 추가
age_groups = ['0~9세', '10대', '20대', '30대', '40대', '50대', '60대', '70대', '80대', '90대', '100세이상']
for group in age_groups:
    df[group] = df['남' + group] + df['여' + group]

# 비교할 동 목록
regions = ['율전동', '연무동', '권선동', '이의동']

# 각 동별 데이터 필터링
df_filtered = df[df['법정구역'].str.contains('|'.join(regions))]

# 데이터를 길게 변환
df_melted = df_filtered.melt(id_vars=['법정구역'], value_vars=age_groups, var_name='연령대', value_name='인구수')

# 법정구역에서 동 이름 추출
df_melted['법정구역1'] = df_melted['법정구역'].str.extract(r'(\w+동)')

# 삭제하는 열 직접 지정하기
df_dropped = df_melted.drop(['법정구역'], axis=1)

df_melted = df_dropped.copy()

df_melted.rename(columns={'법정구역1':'법정구역'}, inplace=True)

# 인구수 컬럼의 콤마 제거 및 정수형 변환
df_melted['인구수'] = df_melted['인구수'].astype(str).str.replace(',', '').astype(int)

# 각 동별, 연령대별 인구수 계산을 위한 피벗 테이블 생성
df_pivot = df_melted.pivot_table(index='연령대', columns='법정구역', values='인구수', aggfunc='sum')

# 막대그래프 순서를 지정
df_pivot = df_pivot[['권선동', '이의동', '율전동', '연무동']]

import matplotlib.font_manager as fm

# 한글 폰트를 설정
plt.rcParams['font.family'] = 'Malgun Gothic'

# 그래프에서 마이너스 폰트가 깨지는 문제를 해결
plt.rcParams['axes.unicode_minus'] = False

# 막대그래프 생성
ax = df_pivot.loc[age_groups].plot(kind='bar', figsize=(14, 8))
ax.set_xlabel('')  # x축 레이블 제거
plt.ylabel('인구수')
plt.title('권선동, 이의동, 율전동, 연무동 연령대별 인구 비교')
plt.legend(title='법정동')
plt.grid(axis='y')
plt.xticks(rotation=65)  # x축 레이블 45도 회전

# 그래프 저장 및 출력
plt.savefig('population_age_group_comparison_bar.png', dpi=300)
plt.show()


#%%
import pandas as pd
import matplotlib.pyplot as plt

# https://jumin.mois.go.kr/ : 법정동별 주민등록 인구통계
df = pd.read_csv(r"C:\Users\goido\Downloads\202405_202405_법정동별 연령별인구현황_월간.csv", encoding='euc-kr')

columns = df.columns.tolist()

# 삭제할 열 인덱스 범위 지정 
start_idx = 1
end_idx = 16
columns_to_drop = columns[start_idx:end_idx]

# 열 삭제
df = df.drop(columns=columns_to_drop)

# 삭제하는 열 직접 지정하기
df.drop(['2024년05월_여_총인구수', '2024년05월_여_연령구간인구수'], axis=1, inplace=True)

# 열 이름 변경
df = df.rename(columns={
    '법정구역':'법정구역',
    '2024년05월_남_0~9세':'남0~9세',
    '2024년05월_남_10~19세':'남10대',
    '2024년05월_남_20~29세':'남20대',
    '2024년05월_남_30~39세':'남30대',
    '2024년05월_남_40~49세':'남40대',
    '2024년05월_남_50~59세':'남50대',
    '2024년05월_남_60~69세':'남60대',
    '2024년05월_남_70~79세':'남70대',
    '2024년05월_남_80~89세':'남80대',
    '2024년05월_남_90~99세':'남90대',
    '2024년05월_남_100세 이상':'남100세이상',
    '2024년05월_여_0~9세':'여0~9세',
    '2024년05월_여_10~19세':'여10대',
    '2024년05월_여_20~29세':'여20대',
    '2024년05월_여_30~39세':'여30대',
    '2024년05월_여_40~49세':'여40대',
    '2024년05월_여_50~59세':'여50대',
    '2024년05월_여_60~69세':'여60대',
    '2024년05월_여_70~79세':'여70대',
    '2024년05월_여_80~89세':'여80대',
    '2024년05월_여_90~99세':'여90대',
    '2024년05월_여_100세 이상':'여100세이상'
})

# 남자와 여자 인구수를 합한 새로운 열 추가
age_groups = ['0~9세', '10대', '20대', '30대', '40대', '50대', '60대', '70대', '80대', '90대', '100세이상']
for group in age_groups:
    df[group] = df['남' + group] + df['여' + group]

# 비교할 동 목록
regions = ['율전동', '연무동', '권선동', '이의동']

# 각 동별 데이터 필터링
df_filtered = df[df['법정구역'].str.contains('|'.join(regions))]

# 데이터를 길게 변환
df_melted = df_filtered.melt(id_vars=['법정구역'], value_vars=age_groups, var_name='연령대', value_name='인구수')

# 법정구역에서 동 이름 추출
df_melted['법정구역1'] = df_melted['법정구역'].str.extract(r'(\w+동)')

# 삭제하는 열 직접 지정하기
df_dropped = df_melted.drop(['법정구역'], axis=1)

df_melted = df_dropped.copy()

df_melted.rename(columns={'법정구역1':'법정구역'}, inplace=True)

# 인구수 컬럼의 콤마 제거 및 정수형 변환
df_melted['인구수'] = df_melted['인구수'].astype(str).str.replace(',', '').astype(int)

# 각 동별, 연령대별 인구수 계산을 위한 피벗 테이블 생성
df_pivot = df_melted.pivot_table(index='연령대', columns='법정구역', values='인구수', aggfunc='sum')

import matplotlib.font_manager as fm

# 한글 폰트를 설정
plt.rcParams['font.family'] = 'Malgun Gothic'

# 그래프에서 마이너스 폰트가 깨지는 문제를 해결
plt.rcParams['axes.unicode_minus'] = False

# 막대그래프 생성
ax = df_pivot.loc[age_groups].plot(kind='bar', figsize=(14, 8))
ax.set_xlabel('')  # x축 레이블 제거
plt.ylabel('인구수')
plt.title('권선동, 이의동, 율전동, 연무동 연령대별 인구 비교')
plt.legend(title='법정동')
plt.grid(axis='y')
plt.xticks(rotation=65)  # x축 레이블 45도 회전

# 그래프 저장 및 출력
plt.savefig('population_age_group_comparison_bar.png', dpi=300)
plt.show()

#%%
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일을 pandas 데이터프레임으로 읽기 (한글 인코딩 설정)
df = pd.read_csv(r"C:\Users\goido\Downloads\202405_202405_법정동별 연령별인구현황_월간.csv", encoding='euc-kr')

columns = df.columns.tolist()

# 삭제할 열 인덱스 범위 지정 
start_idx = 1
end_idx = 16
columns_to_drop = columns[start_idx:end_idx]

# 열 삭제
df = df.drop(columns=columns_to_drop)

# 삭제하는 열 직접 지정하기
df.drop(['2024년05월_여_총인구수', '2024년05월_여_연령구간인구수'], axis=1, inplace=True)

# 열 이름 변경
df = df.rename(columns={
    '법정구역':'법정구역',
    '2024년05월_남_0~9세':'남0~9세',
    '2024년05월_남_10~19세':'남10대',
    '2024년05월_남_20~29세':'남20대',
    '2024년05월_남_30~39세':'남30대',
    '2024년05월_남_40~49세':'남40대',
    '2024년05월_남_50~59세':'남50대',
    '2024년05월_남_60~69세':'남60대',
    '2024년05월_남_70~79세':'남70대',
    '2024년05월_남_80~89세':'남80대',
    '2024년05월_남_90~99세':'남90대',
    '2024년05월_남_100세 이상':'남100세이상',
    '2024년05월_여_0~9세':'여0~9세',
    '2024년05월_여_10~19세':'여10대',
    '2024년05월_여_20~29세':'여20대',
    '2024년05월_여_30~39세':'여30대',
    '2024년05월_여_40~49세':'여40대',
    '2024년05월_여_50~59세':'여50대',
    '2024년05월_여_60~69세':'여60대',
    '2024년05월_여_70~79세':'여70대',
    '2024년05월_여_80~89세':'여80대',
    '2024년05월_여_90~99세':'여90대',
    '2024년05월_여_100세 이상':'여100세이상'
})

# 남자와 여자 인구수를 합한 새로운 열 추가
age_groups = ['0~9세', '10대', '20대', '30대', '40대', '50대', '60대', '70대', '80대', '90대', '100세이상']
for group in age_groups:
    df[group] = df['남' + group] + df['여' + group]

# 비교할 동 목록
regions = ['율전동', '연무동', '권선동', '이의동']

# 각 동별 데이터 필터링
df_filtered = df[df['법정구역'].str.contains('|'.join(regions))]

# 데이터를 길게 변환
df_melted = df_filtered.melt(id_vars=['법정구역'], value_vars=age_groups, var_name='연령대', value_name='인구수')

# 법정구역에서 동 이름 추출
df_melted['법정구역1'] = df_melted['법정구역'].str.extract(r'(\w+동)')

# 삭제하는 열 직접 지정하기
# df_dropped = df_melted.drop(['법정구역', '비교동'], axis=1)

df_dropped.rename(columns={'법정구역1':'법정구역'}, inplace=True)

df_melted = df_dropped.copy()

# 인구수 컬럼의 콤마 제거 및 정수형 변환
df_melted['인구수'] = df_melted['인구수'].astype(str).str.replace(',', '').astype(int)

# 각 동별, 연령대별 인구수 계산을 위한 피벗 테이블 생성
df_pivot = df_melted.pivot_table(index='연령대', columns='법정구역', values='인구수', aggfunc='sum')

# 막대그래프 생성
df_pivot.loc[age_groups].plot(kind='bar', figsize=(14, 8))
plt.xlabel('연령대')
plt.ylabel('인구수')
plt.title('율전동, 연무동, 권선동, 이의동 연령대별 인구 비교')
plt.legend(title='법정동')
plt.grid(axis='y')
plt.xticks(rotation=65)  # x축 레이블 45도 회전

# 그래프 저장 및 출력
plt.savefig('population_age_group_comparison_bar.png', dpi=300)
plt.show()


#%%
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일을 pandas 데이터프레임으로 읽기 (한글 인코딩 설정)
df = pd.read_csv(r"C:\Users\goido\Downloads\202405_202405_법정동별 연령별인구현황_월간.csv", encoding='euc-kr')

columns = df.columns.tolist()

# 삭제할 열 인덱스 범위 지정 
start_idx = 1
end_idx = 16
columns_to_drop = columns[start_idx:end_idx]

# 열 삭제
df = df.drop(columns=columns_to_drop)

# 삭제하는 열 직접 지정하기
df.drop(['2024년05월_여_총인구수', '2024년05월_여_연령구간인구수'], axis=1, inplace=True)

# 열 이름 변경
df = df.rename(columns={
    '법정구역':'법정구역',
    '2024년05월_남_0~9세':'남0~9세',
    '2024년05월_남_10~19세':'남10대',
    '2024년05월_남_20~29세':'남20대',
    '2024년05월_남_30~39세':'남30대',
    '2024년05월_남_40~49세':'남40대',
    '2024년05월_남_50~59세':'남50대',
    '2024년05월_남_60~69세':'남60대',
    '2024년05월_남_70~79세':'남70대',
    '2024년05월_남_80~89세':'남80대',
    '2024년05월_남_90~99세':'남90대',
    '2024년05월_남_100세 이상':'남100세이상',
    '2024년05월_여_0~9세':'여0~9세',
    '2024년05월_여_10~19세':'여10대',
    '2024년05월_여_20~29세':'여20대',
    '2024년05월_여_30~39세':'여30대',
    '2024년05월_여_40~49세':'여40대',
    '2024년05월_여_50~59세':'여50대',
    '2024년05월_여_60~69세':'여60대',
    '2024년05월_여_70~79세':'여70대',
    '2024년05월_여_80~89세':'여80대',
    '2024년05월_여_90~99세':'여90대',
    '2024년05월_여_100세 이상':'여100세이상'
})

# 남자와 여자 인구수를 합한 새로운 열 추가
age_groups = ['0~9세', '10대', '20대', '30대', '40대', '50대', '60대', '70대', '80대', '90대', '100세이상']
for group in age_groups:
    df[group] = df['남' + group] + df['여' + group]

# 비교할 동 목록
regions = ['율전동', '연무동', '권선동', '이의동']

# 각 동별 데이터 필터링
df_filtered = df[df['법정구역'].str.contains('|'.join(regions))]

# 데이터를 길게 변환
df_melted = df_filtered.melt(id_vars=['법정구역'], value_vars=age_groups, var_name='연령대', value_name='인구수')

# 법정구역에서 동 이름 추출
df_melted['법정구역1'] = df_melted['법정구역'].str.extract(r'(\w+동)')

# 삭제하는 열 직접 지정하기
# df_dropped = df_melted.drop(['법정구역', '비교동'], axis=1)

df_dropped.rename(columns={'법정구역1':'법정구역'}, inplace=True)

df_melted = df_dropped.copy()

# 인구수 컬럼의 콤마 제거 및 정수형 변환
df_melted['인구수'] = df_melted['인구수'].astype(str).str.replace(',', '').astype(int)

# 각 동별, 연령대별 인구수 계산을 위한 피벗 테이블 생성
df_pivot = df_melted.pivot_table(index='연령대', columns='법정구역', values='인구수', aggfunc='sum')

# 막대그래프 생성
df_pivot.loc[age_groups].plot(kind='bar', figsize=(14, 8))
plt.xlabel('연령대')
plt.ylabel('인구수')
plt.title('율전동, 연무동, 권선동, 이의동 연령대별 인구 비교')
plt.legend(title='법정구역')
plt.grid(axis='y')

# 그래프 저장 및 출력
plt.savefig('population_age_group_comparison_bar.png', dpi=300)
plt.show()
