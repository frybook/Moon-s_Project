# -*- coding: utf-8 -*-
# 주차지수 : 심각도(공간부족) * 발생도(수요) * 검출도(예측)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

# 1. 데이터 수집 (예시 데이터 생성)
np.random.seed(0)
data = {
    'Location': ['Loc' + str(i) for i in range(1, 101)],
    'Frequency': np.random.randint(1, 100, 100),
    'Severity': np.random.randint(1, 10, 100),
    'Detection': np.random.randint(1, 10, 100)
}
df = pd.DataFrame(data)

# 2. 데이터 전처리
scaler = MinMaxScaler()
df[['Frequency_scaled', 'Severity_scaled', 'Detection_scaled']] = scaler.fit_transform(df[['Frequency', 'Severity', 'Detection']])

# 3. FEMA 분석
df['RPN'] = df['Frequency_scaled'] * df['Severity_scaled'] * df['Detection_scaled']

# 4. 클러스터링 분석
kmeans = KMeans(n_clusters=3, random_state=0)
df['Cluster'] = kmeans.fit_predict(df[['RPN']])

# 5. 결과 시각화
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='Frequency', y='Severity', size='Detection', hue='Cluster', palette='viridis')
plt.title('Illegal Parking Analysis - FEMA')
plt.xlabel('Frequency')
plt.ylabel('Severity')
plt.show()

# 6. 상위 10개 위험 지역 식별
top_10_risk_areas = df.nlargest(10, 'RPN')
print("Top 10 High-Risk Areas for Illegal Parking:")
print(top_10_risk_areas[['Location', 'RPN']])

# 7. 클러스터별 특성 분석
cluster_analysis = df.groupby('Cluster').agg({
    'Frequency': 'mean',
    'Severity': 'mean',
    'Detection': 'mean',
    'RPN': 'mean'
}).round(2)
print("\nCluster Analysis:")
print(cluster_analysis)

# 8. 시계열 분석 (예시 - 실제 데이터에서는 날짜 정보가 필요합니다)
df['Date'] = pd.date_range(start='2023-01-01', periods=100, freq='D')
time_series = df.groupby('Date')['Frequency'].sum().reset_index()

plt.figure(figsize=(12, 6))
plt.plot(time_series['Date'], time_series['Frequency'])
plt.title('Illegal Parking Frequency Over Time')
plt.xlabel('Date')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# FMEA 분석: 빈도(Frequency), 심각도(Severity), 감지 난이도(Detection)를 곱하여 
# RPN(Risk Priority Number)을 계산합니다.
# 클러스터링 분석: K-means 알고리즘을 사용하여 RPN 기반으로 지역을 군집화합니다.
# 결과 시각화: 산점도를 통해 불법주차 문제의 패턴을 시각화합니다.
# 상위 위험 지역 식별: RPN이 높은 상위 10개 지역을 식별합니다.
# 클러스터별 특성 분석: 각 클러스터의 평균 특성을 분석합니다.
# 시계열 분석: 시간에 따른 불법주차 빈도 변화를 분석합니다.

# 이 분석을 통해 불법주차 문제가 가장 심각한 지역을 식별하고, 시간에 따른 
# 패턴을 파악할 수 있습니다. 이를 바탕으로 효과적인 해결 전략을 수립할 수 있습니다. 
# 실제 상황에서는 더 많은 데이터(예: 정확한 위치 정보, 시간대별 데이터, 
# 주차 공간 정보 등)를 활용하여 분석의 정확도를 높일 수 있습니다.