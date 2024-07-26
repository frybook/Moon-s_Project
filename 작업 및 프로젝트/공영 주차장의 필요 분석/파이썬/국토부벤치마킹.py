# -*- coding: utf-8 -*-
import pandas as pd

# 벤치마킹 중인 국토부 주차장 분석 자료입니다.
# http://www.geobigdata.go.kr/portal/analysis/standardModel.do

busulpark = pd.read_csv(r"C:\Users\Charlie\Downloads\parking_lot_buseol (1).csv")
nowpepark = pd.read_csv(r"C:\Users\Charlie\Downloads\parking_lot_nohoe.csv")
nosangpark = pd.read_csv(r"C:\Users\Charlie\Downloads\parking_lot_ns.csv", encoding='euc-kr')

congpark = pd.read_csv(r"C:\Users\Charlie\Downloads\RECAP_TITLE_TOT_PARKING.csv")

car = pd.read_csv(r"C:\Users\Charlie\Downloads\gm_car_reg_index.csv", encoding='euc-kr')
levy = pd.read_csv(r"C:\Users\Charlie\Downloads\parking_bust_geocoding.csv")

#%%
import geopandas as gpd
import folium
from shapely.geometry import Point

# 쉐이프파일 경로
shapefile_path = r"C:\Users\Charlie\Downloads\umd\LSMD_ADM_SECT_UMD_41.shp"

# 쉐이프파일 읽기
gdf = gpd.read_file(shapefile_path)

# 좌표계 확인 및 변환 (EPSG:4326로 변환)
if gdf.crs != "EPSG:4326":
    gdf = gdf.to_crs(epsg=4326)

# 투영된 좌표계로 변환 (EPSG:3857)
gdf_projected = gdf.to_crs(epsg=3857)

# 중심점 계산 (투영된 좌표계에서)
centroid_projected = gdf_projected.geometry.centroid
center_projected = [centroid_projected.y.mean(), centroid_projected.x.mean()]

# 중심점을 포인트 객체로 생성
center_point_projected = Point(center_projected[1], center_projected[0])

# 중심점을 지리적 좌표계로 변환
center_point_geographic = gpd.GeoSeries([center_point_projected], crs="EPSG:3857").to_crs(epsg=4326)

# Folium에서 사용할 중심 좌표 추출
center = [center_point_geographic.geometry.y.values[0], center_point_geographic.geometry.x.values[0]]

# Folium 맵 생성
m = folium.Map(location=center, zoom_start=10)

# GeoDataFrame을 GeoJSON으로 변환 후 맵에 추가
folium.GeoJson(gdf).add_to(m)

# 결과를 HTML 파일로 저장 (경로를 지정)
html_output_path = r'C:\Users\Charlie\Downloads\umd\output_map.html'
m.save(html_output_path)

print(f"지도 HTML 파일이 생성되었습니다: {html_output_path}")



#%%
import geopandas as gpd
import folium
from shapely.geometry import Point

# 쉐이프파일 경로
shapefile_path = r"C:\Users\Charlie\Downloads\(B100)국토통계_인구정보-총 인구 수(전체)-(격자) 100M_경기도 수원시_202404\nlsp_021001001.shp"

# 쉐이프파일 읽기
gdf = gpd.read_file(shapefile_path)

# 좌표계 확인 및 변환 (EPSG:4326로 변환)
if gdf.crs != "EPSG:4326":
    gdf = gdf.to_crs(epsg=4326)

# 투영된 좌표계로 변환 (EPSG:3857)
gdf_projected = gdf.to_crs(epsg=3857)

# 중심점 계산 (투영된 좌표계에서)
centroid_projected = gdf_projected.geometry.centroid
center_projected = [centroid_projected.y.mean(), centroid_projected.x.mean()]

# 중심점을 포인트 객체로 생성
center_point_projected = Point(center_projected[1], center_projected[0])

# 중심점을 지리적 좌표계로 변환
center_point_geographic = gpd.GeoSeries([center_point_projected], crs="EPSG:3857").to_crs(epsg=4326)

# Folium에서 사용할 중심 좌표 추출
center = [center_point_geographic.geometry.y.values[0], center_point_geographic.geometry.x.values[0]]

# Folium 맵 생성
m = folium.Map(location=center, zoom_start=10)

# GeoDataFrame을 GeoJSON으로 변환 후 맵에 추가
folium.GeoJson(gdf).add_to(m)

# 결과를 HTML 파일로 저장 (경로를 지정)
output_path = r'C:\Users\Charlie\Downloads\umd\output1.html'
m.save(output_path)

print(f"지도 HTML 파일이 생성되었습니다: {output_path}")

#%%
# 인구 격자 만들기 작업 중
import geopandas as gpd
import pandas as pd
import folium
from shapely.geometry import Point

# DBF 파일 경로
dbf_path = r"C:\Users\Charlie\Downloads\(B100)국토통계_인구정보-총 인구 수(전체)-(격자) 100M_경기도 수원시_202404\nlsp_021001001.dbf"
shp_path = dbf_path.replace(".dbf", ".shp")  # 관련된 쉐이프파일 경로

# DBF 파일 읽기
df = gpd.read_file(dbf_path)

# 쉐이프파일 읽기
gdf = gpd.read_file(shp_path)

# 좌표계 확인 및 변환 (EPSG:4326로 변환)
if gdf.crs != "EPSG:4326":
    gdf = gdf.to_crs(epsg=4326)

# 인구 데이터가 있는 열 이름 (예: 'POPULATION')
population_column = 'POPULATION'

# Folium 맵 생성 (중심 좌표는 임의로 설정, 필요시 수정)
center = [gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()]
m = folium.Map(location=center, zoom_start=10)

# GeoDataFrame을 GeoJSON으로 변환 후 맵에 추가
folium.GeoJson(gdf).add_to(m)

# 인구 데이터를 색상으로 시각화
gdf[population_column] = gdf[population_column].astype(float)  # 인구 데이터 타입 변환
folium.Choropleth(
    geo_data=gdf,
    name="choropleth",
    data=gdf,
    columns=[gdf.index, population_column],
    key_on="feature.id",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Population"
).add_to(m)

# 결과를 HTML 파일로 저장 (경로를 지정)
html_output_path = r'C:\Users\Charlie\Downloads\umd\output_map.html'
m.save(html_output_path)

print(f"지도 HTML 파일이 생성되었습니다: {html_output_path}")
