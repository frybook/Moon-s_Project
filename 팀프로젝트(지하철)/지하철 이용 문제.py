
# 일일 이용객
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
mpl.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False
import matplotlib.font_manager as fm
font_files = fm.findSystemFonts(fontpaths=['C:/Users/moon/AppData/Local/Microsoft/Windows/Fonts'])
for fpath in font_files:
    fm.fontManager.addfont(fpath)
    
#%% 문제점 파악
df = pd.read_csv('기사제목.csv')
print(df)


#%%
population = pd.read_excel('24년_지역별_인구수.xlsx')
Population_near_Seoul = population.iloc[1] + population.iloc[9] # 서울과 근교 경기도의 합
Percentage_of_population_near_Seoul = np.array(Population_near_Seoul.iloc[1]*100/population.iloc[0,1],dtype=np.float16) # 전체 인구수에 차지하는 서울근교에 비율
b = population.iloc[1:10]
a = population.iloc[[0,1,9]]
#%%
plt.figure(figsize=(8, 8))
plt.pie(b['인구수'], labels=b['행정구역(시군구)별'], autopct='%1.1f%%', startangle=140)
plt.title('지역별 인구수')
plt.axis('equal')
plt.show()
#%%
subway_people = pd.read_csv("서울시 지하철 호선별 역별 시간대별 승하차 인원 정보.csv", encoding='euc-kr')


#%%
# 2023.01 그 전 데이터는 제외
for i in subway_people.index:
    if int(subway_people.loc[i, '사용월']) == 202301:
        break
subway_people = subway_people.loc[:9246, :]
#%%

# 승차인원만 추출
in_df = subway_people.columns.tolist()[:3]
for a in subway_people.columns.tolist():
    if a.find('승차') != -1:
        in_df.append(a)
in_df1 = subway_people[in_df]
plt.rcParams['font.size'] = 11

#%%
# # 승차인원만 합계 구하기
in_df1['승차합계'] = in_df1[[column for column in in_df1.columns if '승차' in column]].sum(axis=1)
# in_df1[[column for column in in_df1.columns if '승차인원' in column]].sum(axis=1)
#%%
# 상위 15개 지하철역 추출
top_15_stations = in_df1.groupby('지하철역')['승차합계'].sum().nlargest(15)

# 막대 그래프 그리기
ax = top_15_stations.plot(kind='bar')

# 각 막대 위에 값 표시 (단위: 백만 명)
for i in ax.patches:
    ax.text(i.get_x() + i.get_width() / 2, i.get_height(), f"{i.get_height() / 1000000:.1f}", ha='center', va='bottom')
# 축 레이블 추가
plt.ylabel('승차인원합계(백만 명)')

# 제목 추가
plt.title('서울 지하철 승차인원 top 15(23.1~24.3 기준)')

# 그래프 표시
plt.show()











#%%
# 서울과 경기권에 인구 비율은 전체에 44.88% 그 많은 인구가 이용하는 지하철에 일일 이용객을 알아보자

mon_2310 = pd.read_csv('CARD_SUBWAY_MONTH_202310.csv', encoding='cp949')
mon_2311 = pd.read_csv('CARD_SUBWAY_MONTH_202311.csv', encoding='cp949')
mon_2312 = pd.read_csv('CARD_SUBWAY_MONTH_202312.csv', encoding='cp949')
mon_2401 = pd.read_csv('CARD_SUBWAY_MONTH_202401.csv', encoding='cp949')
mon_2402 = pd.read_csv('CARD_SUBWAY_MONTH_202402.csv', encoding='cp949')
# 승차총승객수로 상위 1000개 역 분리
mon10 = mon_2310.sort_values(by="승차총승객수", ascending=False).head(1000)
mon11 = mon_2311.sort_values(by="승차총승객수", ascending=False).head(1000)
mon12 = mon_2312.sort_values(by="승차총승객수", ascending=False).head(1000)
mon01 = mon_2401.sort_values(by="승차총승객수", ascending=False).head(1000)
mon02 = mon_2402.sort_values(by="승차총승객수", ascending=False).head(1000)
# 1달간 승차총승객수에서 역명이 중복되는 값확인해서 상위 100개 추출
# 평균적으로 사람들이 많이 타는 역
mon_10 = mon10['역명'].value_counts().head(100)
mon_11 = mon11['역명'].value_counts().head(100)
mon_12 = mon12['역명'].value_counts().head(100)
mon_01 = mon01['역명'].value_counts().head(100)
mon_02 = mon02['역명'].value_counts().head(100)
# 5개월중에 상위 역 추출
df = pd.concat([mon_10, mon_11, mon_12, mon_01, mon_02],join='inner')
c = df.reset_index(drop=False)
d = c.groupby('역명').sum()
# 상위
result = d.sort_values(by='count', ascending=False)
result_A = result['count'].to_list()
#%%
plt.figure(figsize=(14, 10))
plt.bar(result.index,result_A,color = '#e35f62',width= 0.8)
plt.xticks(rotation=90, ha='right')
plt.show()
#%%
subway_people = pd.read_excel("서울시 지하철 호선별 역별 시간대별 승하차 인원 정보.xlsx")

# '여의도'역만 추출
subway_df = subway_people[subway_people['지하철역'] == '여의도']


# 승차 및 하차 데이터 분리
subway_df_on = [column for column in subway_df.columns if '승차' in column]
up = subway_df[subway_df_on]

subway_df_off = [column for column in subway_df.columns if '하차' in column]
down = subway_df[subway_df_off]

# 데이터 월별 평균 계산
subway_df_on = up.mean()
subway_df_off = down.mean()


plt.rcParams['font.size'] = 8

# 다중 막대그래프 그리기
w = 0.35
nrow = subway_df_on.shape[0] # 행의 갯수
idx = np.arange(nrow) #행의 갯수

fig, ax = plt.subplots(figsize=(10, 5))
ax.set_title('여의도역 시간대별 승하차 인원 현황')
ax.set_xlabel('시간대')
ax.set_ylabel('승객(명)')
bars1 = ax.bar(idx - w/2, subway_df_on.values, width=w, label='승차')
bars2 = ax.bar(idx + w/2, subway_df_off.values, width=w, label='하차')

# 막대 위에 값 표시 (천단위로)
for i in bars1:
    ax.text(i.get_x() + i.get_width() / 2, i.get_height(), f"{i.get_height() / 1000:.2f}", ha='center', va='bottom')

for i in bars2:
    ax.text(i.get_x() + i.get_width() / 2, i.get_height(), f"{i.get_height() / 1000:.2f}", ha='center', va='bottom')

# x축에 인덱스 넣기
ax.set_xticks(idx)
ax.set_xticklabels(subway_df_on.index, rotation=30)
ax.legend(ncol=2)
plt.savefig('sci.png', dpi=300)
plt.show()
#%%
subway_people = pd.read_excel("서울시 지하철 호선별 역별 시간대별 승하차 인원 정보.xlsx")
subway_df = subway_people[subway_people['지하철역'] == '홍대입구']


# 승차 및 하차 데이터 분리
subway_df_on = [column for column in subway_df.columns if '승차' in column]
up = subway_df[subway_df_on]


subway_df_off = [column for column in subway_df.columns if '하차' in column]
down = subway_df[subway_df_off]

# 데이터 월별 평균 계산
subway_df_on = up.mean()
subway_df_off = down.mean()

plt.rcParams['font.size'] = 8

# 다중 막대그래프 그리기
w = 0.35
nrow = subway_df_on.shape[0] # 행의 갯수
idx = np.arange(nrow) #행의 갯수

fig, ax = plt.subplots(figsize=(10, 5))
ax.set_title('홍대입구역 시간대별 승하차 인원 현황')
ax.set_xlabel('시간대')
ax.set_ylabel('승객(명)')
bars1 = ax.bar(idx - w/2, subway_df_on.values, width=w, label='승차')
bars2 = ax.bar(idx + w/2, subway_df_off.values, width=w, label='하차')

# 막대 위에 값 표시 (천단위로)
for i in bars1:
    ax.text(i.get_x() + i.get_width() / 2, i.get_height(), f"{i.get_height() / 1000:.2f}", ha='center', va='bottom')

for i in bars2:
    ax.text(i.get_x() + i.get_width() / 2, i.get_height(), f"{i.get_height() / 1000:.2f}", ha='center', va='bottom')

# x축에 인덱스 넣기
ax.set_xticks(idx)
ax.set_xticklabels(subway_df_on.index, rotation=30)
ax.legend(ncol=2)
plt.savefig('hongdae.png', dpi=300)
plt.show()

#%%
'''
서울교통공사 1-8호선 30분 단위 평균 혼잡도로 30분간 지나는 열차들의 평균 혼잡도
(정원대비 승차인원으로, 승차인과 좌석수가 일치할 경우를 혼잡도 34%로 산정) 입니다.
(단위: %).
 서울교통공사 혼잡도 데이터는 요일구분(평일, 토요일, 일요일),
 호선, 역번호, 역명, 상하선구분, 30분단위 별 혼잡도 데이터로 구성되어 있습니다.
'''
# 조사한 상위역중 2역을 중심으로 혼잡도,
data = pd.read_excel('여의도,홍대입구_시간별_혼잡도.xlsx')
# 평일부분만 추출
weekday_data = data.iloc[[0,1,6,7]]
# 평일에 시간부분만 추출
weekday_data_A = weekday_data.iloc[:,5:][weekday_data.iloc[:, 5:] > 50]
# 시간부분에 결측값이 2개이상인 열은 제외해서 조금더 확인
weekday_data_df = weekday_data_A.dropna(axis=1,thresh=weekday_data_A.shape[0]-2)
weekday_data_df.reset_index(drop=True, inplace=True)
# 출발역상하 = ['여의도상선','여의도하선','홍대입구내선','홍대입구외선']
weekday_data_df.index = ['여의도상선','여의도하선','홍대입구내선','홍대입구외선']
weekday_data_df = weekday_data_df.rename_axis('출발역상하')
print(weekday_data_df)
#%%
all_A = pd.read_excel('평일 여의도역 지하철 운행 정보.xlsx')
all_B = pd.read_excel('평일 홍대입구역 지하철 운행 정보.xlsx')
all_A = all_A.count()
all_B = all_B.count()
all_A = pd.DataFrame(all_A)
all_B = pd.DataFrame(all_B)
all_A_values = all_A[0].to_list()
all_B_values = all_B[0].to_list()
#%% 바그래프
plt.figure(figsize=(12, 8))
plt.plot(all_A.index,all_A_values,color = '#e35f62')
plt.xticks(rotation=45, ha='right')
plt.xlabel('운행 시간')
plt.ylabel('열차운행수')
plt.title('여의도역 열차운행')
plt.xticks(['상행(5시)','상행(12시)','상행(24시)','하행(5시)','하행(12시)','하행(24시)'])
plt.show()
#%%
plt.figure(figsize=(12, 8))
plt.plot(all_B.index,all_B_values,color = '#e35f62')
plt.xticks(rotation=45, ha='right')
plt.xlabel('운행 시간')
plt.ylabel('열차운행수')
plt.title('여의도역 열차운행')
plt.xticks(['상행(5시)','상행(12시)','상행(24시)','하행(5시)','하행(12시)','하행(24시)'])
plt.show()





#%%
# 사람들에 혼잡도가 높은 시간대는 7시부터 9시까지가 그리고 17시부터 19시까지가 제일 많은것을확인
data_A = pd.read_excel('여의도역 7시~9시 배차간격.xlsx')
data_B = pd.read_excel('홍대입구역 7시~9시 배차간격.xlsx')
index_length_A = data_A.count()
index_length_A = pd.DataFrame(index_length_A)
index_length_A.rename(columns={0 : '열차운행수'},inplace=True)
index_length_B = data_B.count()
index_length_B = pd.DataFrame(index_length_B)
index_length_B.rename(columns={0 : '열차운행수'},inplace=True)
index_length_A.values
#%%
# 그래프
b = index_length_A['열차운행수'].to_list()

plt.figure(figsize=(8, 6))
plt.bar(index_length_A.index,b,color = ['skyblue','r','orange','pink'])

# x축 이름 기울기
plt.xticks(rotation=45, ha='right')
plt.xlabel('운행 시간')
plt.ylabel('열차운행수')
plt.title('여의도역 열차운행')

plt.tight_layout()
plt.show()
#%%
c = index_length_B.index.to_list()
d = index_length_B['열차운행수'].to_list()


plt.figure(figsize=(8, 6))
plt.bar(c,d,color = ['skyblue','r','orange','pink'])

# x축 이름 기울기
plt.xticks(rotation=45, ha='right')
plt.xlabel('운행 시간')
plt.ylabel('열차운행수')
plt.title('홍대입구역 열차운행')

plt.tight_layout()
plt.show()
