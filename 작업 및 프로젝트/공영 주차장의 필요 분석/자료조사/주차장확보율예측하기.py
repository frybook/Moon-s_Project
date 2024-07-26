# -*- coding: utf-8 -*-
# 주차장 확보율 2020년, 2021년도 결측치 자료를 ARIMA 모델을 사용하여 보완 성공
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

# 엑셀 파일에서 데이터프레임 로드 : 경로는 바꿔야 함
df = pd.read_excel("주차장확보율.xlsx")

# '데이터 없음'을 np.nan으로 변환
df.replace(' 데이터 없음', np.nan, inplace=True)

# float 타입으로 변환
cols = df.columns[1:]
df[cols] = df[cols].astype(float)

# ARIMA 모델을 사용하여 결측치 보완을 위한 함수 정의
def fill_missing_with_arima(series):
    # 시계열 모델을 위해 인덱스를 시간으로 설정
    series.index = pd.date_range(start='2010', periods=len(series), freq='Y')
    
    # 결측치가 아닌 부분만 모델 피팅
    valid_data = series.dropna().astype(float)
    model = ARIMA(valid_data, order=(1, 1, 1))
    fitted_model = model.fit()
    
    # 결측치 예측
    forecast = fitted_model.predict(start=valid_data.index[-1], end=series.index[-1])
    
    # 결측치 대체
    series[series.isna()] = forecast[series.isna()]
    return series

# 결측치 보완
for i in range(df.shape[0]):
    series = df.iloc[i, 1:]
    if series.isnull().any():
        df.iloc[i, 1:] = fill_missing_with_arima(series).values

print(df)


