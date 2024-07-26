# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

# 인구 증가율 통계 계산
mean_growth_rate = swndf['인구증가율'].mean()
std_growth_rate = swndf['인구증가율'].std()

# 시뮬레이션 함수
def simulate_parking_situation(years, population, cars, parking_spaces, illegal_parking, growth_rate_mean, growth_rate_std):
    population_data = []
    cars_data = []
    parking_spaces_data = []
    illegal_parking_data = []
    fines_data = []

    for _ in range(years):
        population_growth_rate = np.random.normal(growth_rate_mean, growth_rate_std)
        population *= (1 + population_growth_rate)
        cars *= (1 + car_growth_rate)
        parking_spaces *= (1 + parking_space_growth_rate)
        illegal_parking = max(0, (cars - parking_spaces) * 0.1)

        population_data.append(population)
        cars_data.append(cars)
        parking_spaces_data.append(parking_spaces)
        illegal_parking_data.append(illegal_parking)
        fines_data.append(illegal_parking * fine_per_violation)

    return population_data, cars_data, parking_spaces_data, illegal_parking_data, fines_data

# Monte Carlo 시뮬레이션
num_simulations = 1000
results = [simulate_parking_situation(years, initial_population, initial_cars, initial_parking_spaces, initial_illegal_parking, mean_growth_rate, std_growth_rate) for _ in range(num_simulations)]

# 결과 분석
final_populations = [result[0][-1] for result in results]
final_cars = [result[1][-1] for result in results]
final_parking_spaces = [result[2][-1] for result in results]
final_illegal_parkings = [result[3][-1] for result in results]
final_fines = [result[4][-1] for result in results]

# 결과 요약
print(f"{years}년 후 예상 인구 (평균): {np.mean(final_populations):.0f}")
print(f"{years}년 후 예상 자동차 수 (평균): {np.mean(final_cars):.0f}")
print(f"{years}년 후 예상 주차장 면수 (평균): {np.mean(final_parking_spaces):.0f}")
print(f"{years}년 후 예상 불법 주정차 수 (평균): {np.mean(final_illegal_parkings):.0f}")
print(f"{years}년 후 예상 과태료 징수액 (평균): ${np.mean(final_fines):.0f}")

# 결과 시각화
plt.figure(figsize=(12, 8))
plt.hist(final_populations, bins=30, alpha=0.5, label='인구')
plt.hist(final_cars, bins=30, alpha=0.5, label='자동차 수')
plt.hist(final_parking_spaces, bins=30, alpha=0.5, label='주차장 면수')
plt.hist(final_illegal_parkings, bins=30, alpha=0.5, label='불법 주정차 수')
plt.hist(final_fines, bins=30, alpha=0.5, label='과태료 징수액')
plt.xlabel('수량')
plt.ylabel('빈도')
plt.title('주차 상황 시뮬레이션 결과 분포 (Monte Carlo)')
plt.legend()
plt.grid(True)
plt.show()
