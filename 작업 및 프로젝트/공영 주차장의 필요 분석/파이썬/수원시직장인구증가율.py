# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# KOSIS 통계자료 : https://kosis.kr/statHtml/statHtml.do?orgId=350&tblId=TX_35001_A008&vw_cd=MT_OTITLE&list_id=350_35001_B&scrId=&seqNo=&lang_mode=ko&obj_var_id=&itm_id=&conn_path=K2&path=%252Fcommon%252Fmeta_onedepth.jsp
# 2012년도부터 2022년까지 데이터 분석 : 인구자료와 달리 건강보험자료는 2022년도까지만 있음
# 건강보험 적용인구 증가율 

swmdf = pd.read_csv(r"C:\Users\Charlie\Downloads\건강보험적용인구.csv", encoding='euc-kr')

list(swmdf)

# 필요한 열만 선택
swmdf = swmdf[['시군구별',
 '적용인구별',
 '단위',
 '2012 년',
 '2013 년',
 '2014 년',
 '2015 년',
 '2016 년',
 '2017 년',
 '2018 년',
 '2019 년',
 '2020 년',
 '2021 년',
 '2022 년']]

# 필요한 행만 선택
swmdf = swmdf[swmdf['시군구별'].str.contains('수원시')]

# 팔달, 영통, 장안, 권선구 직장가입자수만 선택
swmdf = swmdf.loc[[598, 605, 612, 619]]

swmdf.info()

# 필요없는 열 삭제하기
swmdf.drop(columns=['적용인구별', '단위'], inplace=True)

# 합계 구하기
swmdf.loc['합계',:]=swmdf.loc[:, '2012 년':'2022 년'].sum(axis=0)

# 필요없는 열 삭제하기
swmdf.drop(columns=['시군구별'], inplace=True)

# 필요없는 행 삭제하기
swmdf.drop(index=[598, 605, 612, 619], inplace=True)

swmdf = swmdf.reset_index(drop=True)
swmdf.index = ['합계']

list(swmdf)

# 데이터프레임 전치
swndf = swmdf.transpose()

# 인덱스를 열로 변환하고 열 이름을 변경
swndf = swndf.reset_index().rename(columns={'index': '연도'})
# 열 이름을 변경
swndf.rename(columns={'합계': '인구수'}, inplace=True)

# 연도 추출
swndf['연도'] = swndf['연도'].str[:4].astype(int)

# 증가율 계산
swndf['증가율'] = swndf['인구수'].pct_change()

df = swndf.copy()

df.info()

df['연도'] = df['연도'].astype(str)

# 결과 출력
print(df[['연도', '인구수', '증가율']])

# 전체 기간 평균 증가율 계산 (기하평균 사용)
total_growth_rate = (df['인구수'].iloc[-1] / df['인구수'].iloc[0]) ** (1/12) - 1
print(f"\n전체 기간 평균 연간 증가율: {total_growth_rate:.2%}")
# 전체 기간 평균 연간 증가율 : 3.34%

# 산술 평균 증가율 계산
arithmetic_mean_growth_rate = df['증가율'].mean()
print(f"산술 평균 연간 증가율: {arithmetic_mean_growth_rate:.2%}")
# 산술 평균 연간 증가율 : 4.03%


#%%
# 그래프로 유의미한 의미 분석해 보기
import matplotlib.pyplot as plt
from matplotlib import rc
import seaborn as sns

# 스타일 설정
sns.set_style("whitegrid")
sns.set_palette("deep")

plt.rcParams['font.family']='NanumGothic'
plt.rcParams['axes.unicode_minus']=False

# 1. 인구 수 변화 추이와 증가율을 함께 보여주는 그래프
fig, ax1 = plt.subplots(figsize=(12, 6))

# 인구 수 그래프 (왼쪽 y축)
ax1.plot(df['연도'], df['인구수'], marker='o', linewidth=2, color='blue')
ax1.set_xlabel('연도')
ax1.set_ylabel('인구 수', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# 증가율 그래프 (오른쪽 y축)
ax2 = ax1.twinx()
ax2.plot(df['연도'], df['증가율'], marker='s', linewidth=2, color='red')
ax2.set_ylabel('증가율', color='red')
ax2.tick_params(axis='y', labelcolor='red')

plt.title('수원시 건강보험 직장인구 변화 추이 및 증가율 (2012-2022)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 2. 연도별 인구 수 막대 그래프
plt.figure(figsize=(12, 6))
sns.barplot(x='연도', y='인구수', data=df)
plt.title('수원시 건강보험 직장인구 연도별 변화 (2012-2022)')
plt.xlabel('연도')
plt.ylabel('인구 수')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. 증가율 변화 추이 그래프
plt.figure(figsize=(12, 6))
sns.lineplot(x='연도', y='증가율', data=df.iloc[1:], marker='o')  # 첫 해 제외 (NaN)
plt.title('수원시 건강보험 직장인구 연도별 증가율 변화 (2012-2022)')
plt.xlabel('연도')
plt.ylabel('증가율')
plt.axhline(y=arithmetic_mean_growth_rate, color='r', linestyle='--', label='산술 평균 증가율')
plt.axhline(y=total_growth_rate, color='g', linestyle='--', label='전체 기간 평균 증가율')
plt.legend()
plt.tight_layout()
plt.show()

#%%
# 그래프 한번에 표현하기
import matplotlib.pyplot as plt
from matplotlib import rc
import seaborn as sns

# 스타일 설정
sns.set_style("whitegrid")
sns.set_palette("deep")

plt.rcParams['font.family']='NanumGothic'
plt.rcParams['axes.unicode_minus']=False


# 전체 figure 생성
fig = plt.figure(figsize=(18, 15))

# 1. 인구 수 변화 추이와 증가율을 함께 보여주는 그래프
ax1 = fig.add_subplot(3, 1, 1)

# 인구 수 그래프 (왼쪽 y축)
line1 = ax1.plot(df['연도'], df['인구수'], marker='o', linewidth=2, color='blue', label='인구 수')
ax1.set_xlabel('연도')
ax1.set_ylabel('인구 수', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# 증가율 그래프 (오른쪽 y축)
ax2 = ax1.twinx()
line2 = ax2.plot(df['연도'], df['증가율'], marker='s', linewidth=2, color='red', label='증가율')
ax2.set_ylabel('증가율', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# 범례 추가
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left')

ax1.set_title('수원시 건강보험 직장인구 변화 추이 및 증가율 (2012-2022)')
ax1.grid(True, alpha=0.3)

# 2. 연도별 인구 수 막대 그래프
ax3 = fig.add_subplot(3, 1, 2)
sns.barplot(x='연도', y='인구수', data=df, ax=ax3)
ax3.set_title('수원시 건강보험 직장인구 연도별 변화 (2012-2022)')
ax3.set_xlabel('연도')
ax3.set_ylabel('인구 수')
ax3.tick_params(axis='x', rotation=45)

# 3. 증가율 변화 추이 그래프
ax4 = fig.add_subplot(3, 1, 3)
sns.lineplot(x='연도', y='증가율', data=df.iloc[1:], marker='o', ax=ax4)  # 첫 해 제외 (NaN)
ax4.set_title('수원시 건강보험 직장인구 연도별 증가율 변화 (2012-2022)')
ax4.set_xlabel('연도')
ax4.set_ylabel('증가율')
ax4.axhline(y=arithmetic_mean_growth_rate, color='r', linestyle='--', label='산술 평균 증가율')
ax4.axhline(y=total_growth_rate, color='g', linestyle='--', label='전체 기간 평균 증가율')
ax4.legend()

# 3. 증가율 변화 추이 그래프
ax4 = fig.add_subplot(3, 1, 3)
sns.lineplot(x='연도', y='증가율', data=df.iloc[1:], marker='o', ax=ax4)  # 첫 해 제외 (NaN)
ax4.set_title('수원시 건강보험 직장인구 연도별 증가율 변화 (2012-2022)')
ax4.set_xlabel('연도')
ax4.set_ylabel('증가율')
ax4.axhline(y=arithmetic_mean_growth_rate, color='r', linestyle='--', label='산술 평균 증가율')
ax4.axhline(y=total_growth_rate, color='g', linestyle='--', label='전체 기간 평균 증가율')
ax4.legend()


plt.tight_layout()
plt.savefig('1.png', dpi=300)
plt.show()


#%%
# 3번그래프를 인구증가율은 제외하고 다시 그려봄

# 전체 figure 생성
fig = plt.figure(figsize=(18, 15))

# 1. 인구 수 변화 추이와 증가율을 함께 보여주는 그래프
ax1 = fig.add_subplot(3, 1, 1)

# 인구 수 그래프 (왼쪽 y축)
line1 = ax1.plot(df['연도'], df['인구수'], marker='o', linewidth=2, color='blue', label='인구 수')
ax1.set_xlabel('연도')
ax1.set_ylabel('인구 수', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# 증가율 그래프 (오른쪽 y축)
ax2 = ax1.twinx()
line2 = ax2.plot(df['연도'], df['증가율'], marker='s', linewidth=2, color='red', label='증가율')
ax2.set_ylabel('증가율', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# 범례 추가
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left')

ax1.set_title('수원시 건강보험 직장인구 변화 추이 및 증가율 (2012-2022)')
ax1.grid(True, alpha=0.3)

# 2. 연도별 인구 수 막대 그래프
ax3 = fig.add_subplot(3, 1, 2)
sns.barplot(x='연도', y='인구수', data=df, ax=ax3)
ax3.set_title('수원시 건강보험 직장인구 연도별 변화 (2012-2022)')
ax3.set_xlabel('연도')
ax3.set_ylabel('인구 수')
ax3.tick_params(axis='x', rotation=45)

# 3. 산술 평균 증가율 및 전체 기간 평균 증가율 그래프
ax4 = fig.add_subplot(3, 1, 3)
ax4.set_title('수원시 건강보험 직장인구 연도별 증가율 변화 (2012-2022)')
ax4.set_xlabel('연도')
ax4.set_ylabel('증가율')
ax4.plot(df['연도'], [arithmetic_mean_growth_rate] * len(df), color='r', linestyle='-', label='산술 평균 증가율')
ax4.plot(df['연도'], [total_growth_rate] * len(df), color='g', linestyle='--', label='전체 기간 평균 증가율')
ax4.legend()

# y축 상한선 설정
ax4.set_ylim(top=0.05, bottom=0.01)
# y축 눈금 간격 설정
ax4.yaxis.set_major_locator(plt.MultipleLocator(0.002))  # 원하는 간격으로 설정 (예: 2)

plt.tight_layout()
plt.savefig('1.png', dpi=300)
plt.show()
