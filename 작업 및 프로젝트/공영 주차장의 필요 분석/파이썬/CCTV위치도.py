# -*- coding: utf-8 -*-
# try 1
## 경기데이터드림 : 무인교통단속카메라현황 : 이거는 도로 위에 있는 것임.
# 맨 마지막에 골목에 설치된 무인교통단속 카메라 자료가 있음.(try 3 최종버전 참고)
import pandas as pd
import folium

cctv_df = pd.read_csv(r"C:\Users\Charlie\Downloads\무인교통단속카메라현황(제공표준).csv", encoding='euc-kr')

# '수원시' 데이터만 추출
cctv_df = cctv_df[cctv_df['시군명'] == '수원시']

# 지도 생성 
m = folium.Map(location=[37.2662298, 127.0386787], zoom_start=13)

# CCTV 위치를 지도에 추가
for idx, row in cctv_df.iterrows():
    folium.Marker(
        location=[row['위도'], row['경도']],
        popup=row['설치장소'],
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(m)

# 지도 저장 및 출력
m.save('cctv_map.html')
m

#%%
# try 2
## 경기데이터드림 : CCTV현황
import pandas as pd
import folium

muincctv_df = pd.read_csv(r"C:\Users\Charlie\Downloads\CCTV현황(제공표준).csv", encoding='euc-kr')

cctv_df1 = muincctv_df.copy()

# '수원시'를 포함하는 데이터만 추출
cctv_df1 = cctv_df1[cctv_df1['관리기관명'].str.contains('수원시')]
cctv_df1 = cctv_df1[cctv_df1['설치목적구분'].str.contains('교통단속')]

# 팝업명 간단하게 보이게 하기 위해 필요없는 부분 제거하기
cctv_df1['소재지도로명주소'] = cctv_df1['소재지도로명주소'].str.replace('경기도 수원시 팔달구 ', '')
cctv_df1['소재지도로명주소'] = cctv_df1['소재지도로명주소'].str.replace('경기도 수원시 영통구 ', '')
cctv_df1['소재지도로명주소'] = cctv_df1['소재지도로명주소'].str.replace('경기도 수원시 권선구 ', '')
cctv_df1['소재지도로명주소'] = cctv_df1['소재지도로명주소'].str.replace('경기도 수원시 장안구 ', '')

# '위도' 열에서 NaN 값을 가진 행들을 필터링 : 확인 결과 경도도 같이 없음
nan_latitude_rows = cctv_df1[cctv_df1['위도'].isna()]

# '위도' 열에서 NaN 값을 가진 행 삭제 : 7군데인데, 경미하여 삭제함
df_cleaned = cctv_df1.dropna(subset=['위도'])

cctv_df = df_cleaned

# 지도 생성 
m = folium.Map(location=[37.2662298, 127.0386787], zoom_start=13)

# CCTV 위치를 지도에 추가
for idx, row in cctv_df.iterrows():
    folium.Marker(
        location=[row['위도'], row['경도']],
        popup=row['소재지도로명주소'],
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(m)

# 지도 저장 및 출력
m.save('무인cctv_map.html')
m

#%%
# try3 : 밀집도를 알 수 있도록 업데이트함. 최종 버전임
import pandas as pd
import folium
from folium.plugins import MarkerCluster, HeatMap

# 데이터 로드 및 전처리 (기존 코드와 동일)
muincctv_df = pd.read_csv(r"C:\Users\Charlie\Downloads\CCTV현황(제공표준).csv", encoding='euc-kr')
cctv_df1 = muincctv_df.copy()
cctv_df1 = cctv_df1[cctv_df1['관리기관명'].str.contains('수원시')]
cctv_df1 = cctv_df1[cctv_df1['설치목적구분'].str.contains('교통단속')]

# 주소 정제
for district in ['팔달구', '영통구', '권선구', '장안구']:
    cctv_df1['소재지도로명주소'] = cctv_df1['소재지도로명주소'].str.replace(f'경기도 수원시 {district} ', '')

# NaN 값 처리
cctv_df = cctv_df1.dropna(subset=['위도', '경도'])

# 지도 생성
m = folium.Map(location=[37.2662298, 127.0386787], zoom_start=13)

# 마커 클러스터 생성
marker_cluster = MarkerCluster().add_to(m)

# CCTV 위치를 마커 클러스터에 추가
for idx, row in cctv_df.iterrows():
    folium.Marker(
        location=[row['위도'], row['경도']],
        popup=row['소재지도로명주소'],
        icon=folium.Icon(color='red', icon='camera', prefix='fa')
    ).add_to(marker_cluster)

# 히트맵 데이터 준비
heat_data = [[row['위도'], row['경도']] for idx, row in cctv_df.iterrows()]

# 히트맵 추가
HeatMap(heat_data).add_to(m)

# 지도 저장 및 출력
m.save('무인cctv_distribution_map.html')
m

