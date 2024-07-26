# -*- coding: utf-8 -*-
# 이 코드는 참조용. 아래 코드가 완성본임
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
import geopandas as gpd
from shapely.geometry import Polygon
import matplotlib.font_manager as fm

# 한글 폰트 설정
font_path = r'C:\Users\Charlie\AppData\Local\Microsoft\Windows\Fonts\경기천년제목_Light.ttf'  
font_name = fm.FontProperties(fname=font_path, size=10).get_name()
plt.rc('font', family=font_name)

# 데이터 로드 : 경기데이터드림
df = pd.read_csv(r"C:\Users\Charlie\Downloads\발달상권현황.csv", encoding='euc-kr')

# 다중지역정보를 파싱하여 Polygon으로 변환
def parse_polygon(json_str):
    data = json.loads(json_str)
    if data['type'] == 'Polygon':
        return Polygon(data['coordinates'][0])
    return None

# GeoDataFrame 생성
df['geometry'] = df['다중지역정보'].apply(parse_polygon)
gdf = gpd.GeoDataFrame(df, geometry='geometry')

# 좌표계 설정 (WGS84)
gdf.set_crs(epsg=4326, inplace=True)

# UTM-K 좌표계로 변환
gdf_utm = gdf.to_crs(epsg=5179)

# 중심 좌표 계산
gdf_utm['centroid'] = gdf_utm.centroid

# 면적 계산 (단위: 제곱미터)
gdf_utm['area'] = gdf_utm.area

# GeoDataFrame 시각화
fig, ax = plt.subplots(1, 1, figsize=(10, 6))
gdf_utm.boundary.plot(ax=ax)
plt.title('상권 다중지역정보')
plt.axis('off')  # 축 제거
plt.show()

#%%
# 완성본
import pandas as pd
import json
import folium
from folium import GeoJson
from branca.element import Template, MacroElement

# 데이터 로드 : 경기데이터드림
df = pd.read_csv(r"C:\Users\Charlie\Downloads\발달상권현황.csv", encoding='euc-kr')

# df['점포수'].describe() 결과를 바탕으로 구간 설정
bins = [1, 56, 120, 227, 1386]
labels = ['1단계', '2단계', '3단계', '4단계']
df['점포수_등급'] = pd.cut(df['점포수'], bins=bins, labels=labels, include_lowest=True)

# 각 등급의 데이터 개수 확인
print(df['점포수_등급'].value_counts())
print(f"구간 경계값: {bins}")

# 지도 생성 (수원 중심좌표 사용)
m = folium.Map(location=[37.2643553, 127.0349305], zoom_start=14)

def get_color(점포수_등급):
    """
    점포수_등급에 따라 색상을 반환하는 함수.
    """
    if 점포수_등급 == '1단계':
        return 'green'
    elif 점포수_등급 == '2단계':
        return 'blue'
    elif 점포수_등급 == '3단계':
        return 'orange'
    else:
        return 'red'

# GeoJson 레이어 추가
for idx, row in df.iterrows():
    try:
        # 다중지역정보가 비어있지 않고 유효한 JSON 형식인지 확인
        if pd.notna(row['다중지역정보']):
            geojson = json.loads(row['다중지역정보'])
            GeoJson(
                geojson,
                style_function=lambda feature: {
                    'fillColor': get_color(row['점포수_등급']),
                    'color': 'black',
                    'weight': 2,
                    'fillOpacity': 0.1,
                }
            ).add_to(m)
    except json.JSONDecodeError:
        print(f"다중지역정보 파싱 오류 발생: {row['상권명']}")

# 각 상권의 중심점에 마커 추가
for idx, row in df.iterrows():
    try:
        # 위도와 경도 값이 존재하는지 확인
        if pd.notna(row['위도']) and pd.notna(row['경도']):
            # 점포수 등급에 따라 색상 결정
            color = get_color(row['점포수_등급'])

            folium.CircleMarker(
                location=[row['위도'], row['경도']],
                radius=row['점포수'] / 40,  # 크기 조정 (예: 1/40 비율)
                popup=f"{row['상권명']}<br>점포수: {row['점포수']}개<br>업종정보: {row['업종정보']}",
                tooltip=f"{row['상권명']}<br>점포수: {row['점포수']}개",
                color=color,
                fill=True,
                fill_color=color,
                fill_opacity=0.6
            ).add_to(m)
    except Exception as e:
        print(f"마커 추가 오류 발생: {row['상권명']} - {e}")

# 범례 추가
legend_html = '''
<div style="position: fixed; 
            bottom: 50px; left: 50px; width: 230px; height: 120px; 
            border:2px solid grey; z-index:9999; font-size:14px;
            background-color:white; padding: 10px;">
    <b>점포수 등급</b><br>
    <i style="background:green; width: 10px; height: 10px; display: inline-block;"></i>&nbsp; 1단계: 1 <= 점포수 < 56<br>
    <i style="background:blue; width: 10px; height: 10px; display: inline-block;"></i>&nbsp; 2단계: 56 <= 점포수 < 120<br>
    <i style="background:orange; width: 10px; height: 10px; display: inline-block;"></i>&nbsp; 3단계: 120 <= 점포수 < 227<br>
    <i style="background:red; width: 10px; height: 10px; display: inline-block;"></i>&nbsp; 4단계: 227 <= 점포수 <= 1386<br>
</div>
'''

m.get_root().html.add_child(folium.Element(legend_html))

# HTML 파일로 저장
m.save("상권_지도.html")

print("지도가 '상권_지도.html' 파일로 저장되었습니다.")


