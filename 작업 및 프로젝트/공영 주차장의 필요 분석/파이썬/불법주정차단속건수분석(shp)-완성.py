# -*- coding: utf-8 -*-
import pandas as pd
import folium
from folium.plugins import MarkerCluster
import webbrowser
import geopandas as gpd

# 데이터 로드 및 전처리
df = pd.read_csv(r"E:\workspace\downloadata\경기도_수원시_주정차단속현황_20240122.CSV", encoding='euc-kr')
df1 = pd.read_csv(r"E:\workspace\downloadata\경기도_수원시_주정차단속현황_20221227.csv", encoding='euc-kr')
pdf = pd.concat([df, df1])
pdf['단속건수'] = pdf['단속건수'].str.replace(',', '').astype(int)

# 지도 데이터 준비
geo_json = gpd.read_file(r"E:\workspace\downloadata\경계선자료\emd.shp", encoding='cp949')
geo_json = geo_json[['EMD_CD', 'EMD_KOR_NM', 'geometry']]
geo_json.rename({'EMD_CD':'법정동코드'}, axis=1, inplace=True)

swdf = pd.read_csv(r"E:\workspace\downloadata\경계선자료\법정동코드 전체자료.txt", delimiter='\t', encoding='euc-kr')
swdf = swdf[(swdf['폐지여부'] == "존재") & (swdf['법정동명'].str.contains('수원'))]
swdf['동이름'] = swdf['법정동명'].str.split().str[-1]
swdf = swdf.reset_index(drop=True)

law_code = swdf
law_code['법정동코드'] = law_code['법정동코드'].astype(str).str[:8]

swdf_geojson = geo_json[geo_json['법정동코드'].isin(law_code['법정동코드'])]
merged_df = pd.merge(law_code, swdf_geojson, on='법정동코드', how='left')
geo_json = merged_df
geo_json.rename({'동이름':'단속동'}, axis=1, inplace=True)

# 단속동별 총 단속건수 계산
단속동_집계 = pdf.groupby('단속동')['단속건수'].sum().reset_index()

# 지도 데이터와 단속 데이터 병합
geo_json = pd.merge(geo_json, 단속동_집계, on='단속동', how='left')

# 누락된 지오메트리 제거
geo_json = geo_json.dropna(subset=['geometry'])
geo_json = geo_json.dropna(subset=['단속건수'])

geo_json.to_csv('1.csv')

import pandas as pd
import geopandas as gpd
import folium
from folium.plugins import MarkerCluster

# CSV 파일에서 데이터 로드
geo_json = pd.read_csv(r"E:\workspace\python\1.csv")

# geometry 열을 GeoSeries로 변환
geo_json['geometry'] = gpd.GeoSeries.from_wkt(geo_json['geometry'])

# GeoDataFrame 생성 (여기서 원본 데이터의 CRS를 명시해야 합니다. 
# 예를 들어, EPSG:5174가 한국에서 많이 사용되는 좌표계 중 하나입니다.)
gdf = gpd.GeoDataFrame(geo_json, geometry='geometry', crs="EPSG:5174")

# WGS84 (EPSG:4326)로 변환
gdf = gdf.to_crs("EPSG:4326")

pd.set_option('display.max_columns', None)

print(gdf.head())

# 예를 들어, EPSG:5179를 사용한다고 가정
gdf = gpd.GeoDataFrame(geo_json, geometry='geometry', crs="EPSG:5179")

# 그 다음, WGS84 (EPSG:4326) 좌표계로 변환합니다:
gdf = gdf.to_crs("EPSG:4326")

# 지도 생성 (수원시 중심으로 설정)
m = folium.Map(location=[37.2636, 127.0286], zoom_start=14)

# Choropleth 레이어 추가
folium.Choropleth(
    geo_data=gdf,
    name='불법주정차 단속현황',
    data=gdf,
    columns=['단속동', '단속건수'],
    key_on='feature.properties.단속동',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='단속건수'
).add_to(m)


# GeoJson 레이어 추가 (툴팁 포함)
folium.GeoJson(
    gdf,
    name='단속동 정보',
    tooltip=folium.GeoJsonTooltip(fields=['단속동', '단속건수'], 
                                  aliases=['동 이름', '단속 건수'], 
                                  localize=True)
).add_to(m)

# 마커 클러스터 추가
# marker_cluster = MarkerCluster().add_to(m)

# # 각 단속동의 중심에 마커 추가
# for idx, row in gdf.iterrows():
#     folium.Marker(
#         location=[row.geometry.centroid.y, row.geometry.centroid.x],
#         popup=f"{row['단속동']}: {row['단속건수']}건",
#         tooltip=row['단속동']
#     ).add_to(marker_cluster)

# 레이어 컨트롤 추가
folium.LayerControl().add_to(m)

# 지도 저장
m.save("수원시_불법주정차_단속현황.html")

# 웹 브라우저에서 지도 열기
import webbrowser
webbrowser.open("수원시_불법주정차_단속현황.html")

#%%
# 미완성 : 지도에 팝업내용 텍스트로 표시하기
import folium
from folium.plugins import MarkerCluster

# 지도 생성 (수원시 중심으로 설정)
m = folium.Map(location=[37.2636, 127.0286], zoom_start=12)

# Choropleth 레이어 추가
folium.Choropleth(
    geo_data=gdf,
    name='불법주정차 단속현황',
    data=gdf,
    columns=['단속동', '단속건수'],
    key_on='feature.properties.단속동',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='단속건수'
).add_to(m)

# GeoJson 레이어 추가 (툴팁 포함)
folium.GeoJson(
    gdf,
    name='단속동 정보',
    tooltip=folium.GeoJsonTooltip(fields=['단속동', '단속건수'], 
                                  aliases=['동 이름', '단속 건수'], 
                                  localize=True)
).add_to(m)

# 각 단속동의 중심에 텍스트 추가
for idx, row in gdf.iterrows():
    folium.map.Marker(
        [row.geometry.centroid.y, row.geometry.centroid.x],
        icon=folium.DivIcon(html=f"<div style='font-size: 10pt; color: black;'>{row['단속동']}<br>{row['단속건수']}건</div>")
    ).add_to(m)

# 레이어 컨트롤 추가
folium.LayerControl().add_to(m)

# 지도 저장
m.save("수원시_불법주정차_단속현황.html")

# 웹 브라우저에서 지도 열기
import webbrowser
webbrowser.open("수원시_불법주정차_단속현황.html")