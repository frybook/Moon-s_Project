
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
mpl.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False
#폰트
import matplotlib.font_manager as fm

#%%

# 한국 지도 읽어오기
korea_map = gpd.read_file('C:/Python/Syntex/따로 공부/출산율/TL_SCCO_CTPRVN.json')
korea_map['CTP_KOR_NM'] = korea_map['CTP_KOR_NM'].astype(str)
# 데이터 읽어오기
population_data = pd.read_excel('C:/Python/Syntex/따로 공부/출산율/24년_지역별_인구수.xlsx')

# 인구 데이터를 한국 지도에 포함시키기
merged_data = korea_map.merge(population_data, how='left', left_on='CTP_KOR_NM', right_on='행정구역(시군구)별')

# 지도 표시
fig, ax = plt.subplots(figsize=(10, 8))

# 설정
merged_data.plot(column='인구수', cmap='RdPu', linewidth=1.5, ax=ax, edgecolor='0.7', legend=True, missing_kwds={'color': 'lightgrey'})
plt.text(0.5, 0.95, "(서울.경기) 전체비율에 44%", fontsize=15, ha='center', transform=ax.transAxes)
ax.set_title('24년 지역별 인구 밀도',fontsize=20)
ax.axis('off') 


plt.show()