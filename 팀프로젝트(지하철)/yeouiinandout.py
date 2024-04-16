# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# CSV 파일을 데이터프레임으로 변환
subway_people = pd.read_csv("서울시 지하철 호선별 역별 시간대별 승하차 인원 정보-1.csv", encoding='euc-kr')

# '여의도'역만 추출
subway_df = subway_people[subway_people['지하철역'] == '여의도']


# 승차 및 하차 데이터 분리
subway_df_on = [column for column in subway_df.columns if '승차' in column]
up = subway_df[subway_df_on]

subway_df_off = [column for column in subway_df.columns if '하차' in column]
down = subway_df[subway_df_off]

# 데이터 월별 평균 계산
subway_df_on = up.mean()
subway_df_off = down.mean()


plt.rcParams['font.size'] = 8

# 다중 막대그래프 그리기
w = 0.35
nrow = subway_df_on.shape[0] # 행의 갯수
idx = np.arange(nrow) #행의 갯수

fig, ax = plt.subplots(figsize=(10, 5))
ax.set_title('여의도역 시간대별 승하차 인원 현황')
ax.set_xlabel('시간대')
ax.set_ylabel('승객(명)')
bars1 = ax.bar(idx - w/2, subway_df_on.values, width=w, label='승차')
bars2 = ax.bar(idx + w/2, subway_df_off.values, width=w, label='하차')

# 막대 위에 값 표시 (천단위로)
for i in bars1:
    ax.text(i.get_x() + i.get_width() / 2, i.get_height(), f"{i.get_height() / 1000:.2f}", ha='center', va='bottom')

for i in bars2:
    ax.text(i.get_x() + i.get_width() / 2, i.get_height(), f"{i.get_height() / 1000:.2f}", ha='center', va='bottom')

# x축에 인덱스 넣기
ax.set_xticks(idx)
ax.set_xticklabels(subway_df_on.index, rotation=30)
ax.legend(ncol=2)
plt.savefig('sci.png', dpi=300)
plt.show()
