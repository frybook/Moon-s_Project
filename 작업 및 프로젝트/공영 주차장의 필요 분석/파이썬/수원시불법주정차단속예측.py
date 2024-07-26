# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt

# 데이터 로딩 (기존 코드와 동일)
df_1 = pd.read_csv(r"C:\Users\goido\Downloads\경기도_수원시_주정차단속현황_20211001.csv", encoding='euc-kr')   
df_2 = pd.read_csv(r"C:\Users\goido\Downloads\경기도_수원시_주정차단속현황_20220101.csv", encoding='utf-8')   
df_3 = pd.read_csv(r"C:\Users\goido\Downloads\경기도_수원시_주정차단속현황_20221227 (1).csv", encoding='euc-kr')     
df_4 = pd.read_csv(r"C:\Users\goido\Downloads\경기도_수원시_주정차단속현황_20240122.CSV", encoding='euc-kr')     

# 데이터프레임 병합
merged_df = pd.concat([df_1, df_2, df_3, df_4], ignore_index=True)

# 중복된 자료 중 첫 번째 데이터만 남기고 삭제
merged_df = merged_df.drop_duplicates()

# '단속년월' 열을 datetime 형식으로 변환
merged_df['단속년월'] = pd.to_datetime(merged_df['단속년월'], format='%Y-%m')

# '단속건수'와 '단속원금' 열을 숫자 형식으로 변환
merged_df['단속건수'] = pd.to_numeric(merged_df['단속건수'], errors='coerce')
merged_df['단속원금'] = pd.to_numeric(merged_df['단속원금'], errors='coerce')

# 2021년 1월부터 2023년 12월까지의 데이터 필터링
filtered_df = merged_df[(merged_df['단속년월'] >= '2021-01-01') & (merged_df['단속년월'] <= '2023-12-31')]

# 예측 함수 정의
def predict_next_month(data):
    model = ARIMA(data, order=(1,1,1))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=1)
    return forecast[0]

# 각 동별로 예측 수행 및 결과 저장
predictions = []
for dong in filtered_df['단속동'].unique():
    dong_data = filtered_df[filtered_df['단속동'] == dong].set_index('단속년월')
    monthly_counts = dong_data.resample('M')['단속건수'].sum()
    monthly_fines = dong_data.resample('M')['단속원금'].sum()
    
    next_month_count = predict_next_month(monthly_counts)
    next_month_fine = predict_next_month(monthly_fines)
    
    predictions.append({
        '단속동': dong,
        '예측_단속건수': next_month_count,
        '예측_단속원금': next_month_fine
    })

# 예측 결과를 데이터프레임으로 변환
predictions_df = pd.DataFrame(predictions)
predictions_df = predictions_df.sort_values(by='예측_단속건수', ascending=False)

# 상위 20개 동 추출
top_20_df = predictions_df.head(20)

# 그래프 폰트 설정
font_path = "c:/Windows/Fonts/NanumGothic.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

# 그래프 표시
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(15, 12), sharex=True)

# 단속건수 그래프
bars1 = axes[0].bar(top_20_df['단속동'], top_20_df['예측_단속건수'], color='b', alpha=0.7)
axes[0].set_title('월별 단속건수 예측자료(상위 20개 동)', fontsize=16)
axes[0].set_ylabel('단속건수', fontsize=12)
axes[0].grid(True, axis='y', linestyle='--', alpha=0.7)

# 단속건수 막대 위에 수치 표시
for bar in bars1:
    height = bar.get_height()
    axes[0].text(bar.get_x() + bar.get_width()/2., height,
                 f'{height:.0f}',
                 ha='center', va='bottom')

# 단속원금 그래프
bars2 = axes[1].bar(top_20_df['단속동'], top_20_df['예측_단속원금'], color='r', alpha=0.7)
axes[1].set_title('월별 단속원금 예측자료(상위 20개 동)', fontsize=16)
axes[1].set_ylabel('단속원금', fontsize=12)
axes[1].grid(True, axis='y', linestyle='--', alpha=0.7)

# 단속원금 막대 위에 수치 표시
for bar in bars2:
    height = bar.get_height()
    axes[1].text(bar.get_x() + bar.get_width()/2., height,
                 f'{height:.0f}',
                 ha='center', va='bottom')

plt.xlabel('단속동', fontsize=12)
plt.xticks(rotation=45, ha='right')

# x축 레이블 간격 조정
for ax in axes:
    ax.set_xticks(range(len(top_20_df['단속동'])))
    ax.set_xticklabels(top_20_df['단속동'], rotation=45, ha='right')

plt.tight_layout()
plt.savefig('불법주정차단속예측그래프_상위20', dpi=300, bbox_inches='tight')
plt.show()



#%%
# 아래 스크립트는 전체 동 다 출력됨 : 복잡해서 상위20개동만 출력함
predictions_df = predictions_df.sort_values(by='예측_단속건수', ascending=False)

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "c:/Windows/Fonts/NanumGothic.ttf"
font_name = font_manager.FontProperties(fname = font_path).get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

# 그래프 표시
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(15, 12), sharex=True)

# 단속건수 그래프
bars1 = axes[0].bar(predictions_df['단속동'], predictions_df['예측_단속건수'], color='b', alpha=0.7)
axes[0].set_title('예측 단속건수', fontsize=16)
axes[0].set_ylabel('단속건수', fontsize=12)
axes[0].grid(True, axis='y', linestyle='--', alpha=0.7)

# 단속건수 막대 위에 수치 표시
for bar in bars1:
    height = bar.get_height()
    axes[0].text(bar.get_x() + bar.get_width()/2., height,
                 f'{height:.0f}',
                 ha='center', va='bottom')

# 단속원금 그래프
bars2 = axes[1].bar(predictions_df['단속동'], predictions_df['예측_단속원금'], color='r', alpha=0.7)
axes[1].set_title('예측 단속원금', fontsize=16)
axes[1].set_ylabel('단속원금', fontsize=12)
axes[1].grid(True, axis='y', linestyle='--', alpha=0.7)

# 단속원금 막대 위에 수치 표시
for bar in bars2:
    height = bar.get_height()
    axes[1].text(bar.get_x() + bar.get_width()/2., height,
                 f'{height:.0f}',
                 ha='center', va='bottom')

plt.xlabel('단속동', fontsize=12)
plt.xticks(rotation=90)

# x축 레이블 간격 조정
for ax in axes:
    ax.set_xticks(range(len(predictions_df['단속동'])))
    ax.set_xticklabels(predictions_df['단속동'], rotation=90)

plt.tight_layout()
plt.savefig('불법주정차단속예측그래프', dpi=300, bbox_inches='tight')
plt.show()