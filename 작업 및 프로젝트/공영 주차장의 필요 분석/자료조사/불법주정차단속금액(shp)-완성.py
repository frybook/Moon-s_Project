# -*- coding: utf-8 -*-
# 2023년도 기준 수원 불법주정차 평균단속원금, 총단속원금, 단속건수 지도만들기 스크립트
import pandas as pd
import geopandas as gpd
import folium
from folium.plugins import MarkerCluster
import webbrowser

# 데이터 로드 및 전처리
df = pd.read_csv(r"E:\workspace\downloadata\경기도_수원시_주정차단속현황_20240122.CSV", encoding='euc-kr')

df['단속건수'] = df['단속건수'].str.replace(',', '')  # 쉼표 제거
df['단속건수'] = df['단속건수'].astype(int)  # 정수로 변환

df.info()

# 단속동별 평균 단속원금 계산
단속동_집계 = df.groupby('단속동').agg({
    '단속원금': ['mean', 'sum'],
    '단속건수': 'sum'
}).reset_index()
단속동_집계.columns = ['단속동', '평균단속원금', '총단속원금', '단속건수']
단속동_집계['평균단속원금'] = 단속동_집계['평균단속원금'].round().astype(int)

#%%
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns

# 한글 폰트 설정
font_path = r"c:\Windows\Fonts\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

# 상위 20개 단속건수 데이터 추출
top_20 = 단속동_집계.sort_values(by='단속건수', ascending=False).head(20)

# 막대 그래프 생성
plt.figure(figsize=(12, 8))
barplot = sns.barplot(x='단속건수', y='단속동', data=top_20, palette='viridis', hue='단속동', dodge=False, legend=False)
plt.title('23년 수원시 동별 상위 20개 불법주정차 단속현황', fontsize=15)
plt.xlabel('단속건수', fontsize=12)
plt.ylabel('단속동', fontsize=12)

# 막대 위에 수치 표시
for index, value in enumerate(top_20['단속건수']):
    barplot.text(value + 20, index, str(value), color='black', ha="left", va="center")

plt.tight_layout()
plt.savefig('23년 수원시 동별 상위 20개 불법주정차 단속현황.png')
plt.show()


#%%
## 단속원금 지도 스크립트인데, 금액상으로는 인계동이 광교 등에 밀려서 사용안하는게 
#  좋을 듯 합니다.
# 지도 데이터 준비
geo_json = gpd.read_file(r"E:\workspace\downloadata\경계선자료\emd.shp", encoding='cp949')
geo_json = geo_json[['EMD_CD', 'EMD_KOR_NM', 'geometry']]
geo_json.rename(columns={'EMD_CD': '법정동코드'}, inplace=True)

swdf = pd.read_csv(r"E:\workspace\downloadata\경계선자료\법정동코드 전체자료.txt", delimiter='\t', encoding='euc-kr')
swdf = swdf[(swdf['폐지여부'] == "존재") & (swdf['법정동명'].str.contains('수원'))]
swdf['동이름'] = swdf['법정동명'].str.split().str[-1]
swdf = swdf.reset_index(drop=True)

law_code = swdf
law_code['법정동코드'] = law_code['법정동코드'].astype(str).str[:8]

swdf_geojson = geo_json[geo_json['법정동코드'].isin(law_code['법정동코드'])]
merged_df = pd.merge(law_code, swdf_geojson, on='법정동코드', how='left')
geo_json = merged_df
geo_json.rename(columns={'동이름': '단속동'}, inplace=True)

# 지도 데이터와 단속 데이터 병합
geo_json = pd.merge(geo_json, 단속동_집계, on='단속동', how='left')

# 누락된 지오메트리 제거
geo_json = geo_json.dropna(subset=['geometry', '단속건수'])

# GeoDataFrame 생성 및 좌표계 변환
gdf = gpd.GeoDataFrame(geo_json, geometry='geometry', crs="EPSG:5179")
gdf = gdf.to_crs(epsg=4326)  # WGS84로 변환

# 지도 생성 (수원시 중심으로 설정)
m = folium.Map(location=[37.2636, 127.0286], zoom_start=12)

# Choropleth 레이어 추가 (평균 단속원금 기준)
folium.Choropleth(
    geo_data=gdf.to_json(),
    name='불법주정차 평균 단속원금',
    data=gdf,
    columns=['단속동', '평균단속원금'],
    key_on='feature.properties.단속동',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='평균 단속원금'
).add_to(m)

# GeoJson 레이어 추가 (툴팁 포함)
folium.GeoJson(
    gdf,
    name='단속동 정보',
    style_function=lambda feature: {
        'fillColor': 'transparent',
        'color': 'black',
        'weight': 1,
        'fillOpacity': 0.7,
    },
    tooltip=folium.GeoJsonTooltip(
        fields=['단속동', '평균단속원금', '총단속원금', '단속건수'], 
        aliases=['동 이름', '평균 단속원금', '총 단속원금', '단속 건수'], 
        localize=True,
        style=('background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;')
    ),
    popup=folium.GeoJsonPopup(
        fields=['단속동', '평균단속원금', '총단속원금', '단속건수'],
        aliases=['동 이름', '평균 단속원금', '총 단속원금', '단속 건수'],
        localize=True,
        style='background-color: white; color: #333333; font-family: arial; font-size: 14px; padding: 10px;'
    )
).add_to(m)

# 레이어 컨트롤 추가
folium.LayerControl().add_to(m)

# 지도 저장
m.save("수원시_불법주정차_평균단속원금.html")

# 웹 브라우저에서 지도 열기
webbrowser.open("수원시_불법주정차_평균단속원금.html")

