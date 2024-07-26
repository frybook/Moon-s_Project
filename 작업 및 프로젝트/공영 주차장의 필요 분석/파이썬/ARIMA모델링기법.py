# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import warnings
warnings.filterwarnings("ignore")

# 초기 설정
years = 10  # 시뮬레이션 기간 (년)
initial_population = 100000  # 초기 인구
initial_cars = 50000  # 초기 자동차 수
initial_parking_spaces = 40000  # 초기 주차장 면수
initial_illegal_parking = 5000  # 초기 불법 주정차 수
fine_per_violation = 50  # 위반당 과태료 (달러)

# 수원시 인구 증가율 데이터 로드 및 처리
swpdf = pd.read_csv(r"C:\Users\Charlie\Downloads\101_DT_1B04005N_20240704112830.csv", encoding='euc-kr')
swpdf = swpdf[['행정구역(동읍면)별', '2011 년', '2012 년', '2013 년', '2014 년', '2015 년', '2016 년', '2017 년', '2018 년', '2019 년', '2020 년', '2021 년', '2022 년', '2023 년']]
swndf = swpdf.iloc[66].to_frame()
swndf.rename(columns={66: '인구수'}, inplace=True)
swndf.rename(columns={'행정구역': '연도'}, inplace=True)
swndf.drop(index=0, inplace=True)
swndf['인구수'] = swndf['인구수'].astype(int)
swndf['연도'] = swndf['연도'].str[:4].astype(int)
swndf['인구증가율'] = swndf['인구수'].pct_change()

# ARIMA 모델을 사용하여 인구 증가율 예측
model = ARIMA(swndf['인구수'], order=(5, 1, 0))
model_fit = model.fit()
forecast = model_fit.forecast(steps=years)
population_forecast = forecast.values

# 연도별 인구 데이터 생성
population_data = [initial_population] + list(population_forecast)

# 자동차 및 주차장 면수 증가율
car_growth_rate = 0.03  # 자동차 증가율
parking_space_growth_rate = 0.01  # 주차장 면수 증가율

# 시뮬레이션 함수
def simulate_parking_situation(years, initial_cars, initial_parking_spaces, initial_illegal_parking, population_data):
    cars_data = [initial_cars]
    parking_spaces_data = [initial_parking_spaces]
    illegal_parking_data = [initial_illegal_parking]
    fines_data = [initial_illegal_parking * fine_per_violation]

    for year in range(1, years + 1):
        # 자동차, 주차장 면수 증가
        cars = cars_data[-1] * (1 + car_growth_rate)
        parking_spaces = parking_spaces_data[-1] * (1 + parking_space_growth_rate)

        # 불법 주정차 계산 (자동차 수와 주차장 면수의 차이에 비례)
        illegal_parking = max(0, (cars - parking_spaces) * 0.1)  # 10%가 불법 주정차한다고 가정

        # 데이터 저장
        cars_data.append(cars)
        parking_spaces_data.append(parking_spaces)
        illegal_parking_data.append(illegal_parking)
        fines_data.append(illegal_parking * fine_per_violation)

    return population_data, cars_data, parking_spaces_data, illegal_parking_data, fines_data

# 시뮬레이션 실행
results = simulate_parking_situation(years, initial_cars, initial_parking_spaces, initial_illegal_parking, population_data)

# 결과 시각화
plt.figure(figsize=(12, 8))
plt.plot(range(years + 1), results[0], label='인구')
plt.plot(range(years + 1), results[1], label='자동차 수')
plt.plot(range(years + 1), results[2], label='주차장 면수')
plt.plot(range(years + 1), results[3], label='불법 주정차 수')
plt.plot(range(years + 1), results[4], label='과태료 징수액')
plt.xlabel('년도')
plt.ylabel('수량')
plt.title('주차 상황 시뮬레이션 (ARIMA 기반 인구 예측)')
plt.legend()
plt.grid(True)
plt.show()

# 최종 결과 출력
print(f"{years}년 후:")
print(f"인구: {results[0][-1]:.0f}")
print(f"자동차 수: {results[1][-1]:.0f}")
print(f"주차장 면수: {results[2][-1]:.0f}")
print(f"불법 주정차 수: {results[3][-1]:.0f}")
print(f"과태료 징수액: ${results[4][-1]:.0f}")
