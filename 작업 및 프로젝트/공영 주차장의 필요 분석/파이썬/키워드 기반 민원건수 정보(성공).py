# -*- coding: utf-8 -*-
## 민원 자료는 공공데이터에서 디코딩으로 바로 다운로드 받아야 함.
# 국민권익위원회_민원빅데이터_분석정보_API_2022 : 최다 민원 keyword 정보
# html로 받은 자료를 아래와 같이 전처리함.
from bs4 import BeautifulSoup
import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc

file_path = r"C:\Users\Charlie\Downloads\response_1720593800063.html"

with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html_content, 'html.parser')

# JSON 데이터 추출
json_data_str = soup.text  # HTML 내에 JSON 문자열이 있다고 가정

# JSON 문자열을 파이썬 객체로 변환
data = json.loads(json_data_str)

# DataFrame으로 변환
df = pd.DataFrame(data)

# 기존 열 이름 출력
print("기존 열 이름:", df.columns.tolist())  # 기존 열 이름: ['term', 'df']

# 열 이름 변경
df = df.rename(columns={"term":"민원내용", "df": "민원건수"})

df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1000 entries, 0 to 999
# Data columns (total 2 columns):
#  #   Column  Non-Null Count  Dtype 
# ---  ------  --------------  ----- 
#  0   민원내용    1000 non-null   object
#  1   민원건수    1000 non-null   object
# dtypes: object(2)
# memory usage: 15.8+ KB

# 민원건수 컬럼을 숫자형으로 변환
df['민원건수'] = df['민원건수'].astype(int)

# # 민원건수 기준 상위 20개 추출
df_top20 = df.nlargest(20, '민원건수')
df_top20 = df_top20.sort_values(by='민원건수', ascending=True)

#%%
# 데이터 시각화
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns

# 한글 폰트 설정
font_path = r"C:\Users\Charlie\AppData\Local\Microsoft\Windows\Fonts\경기천년제목_Medium.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

# 그래프 생성
fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.barh(df_top20['민원내용'], df_top20['민원건수'], color='skyblue')

# 특정 막대 그래프의 색상 변경
change_color_indices = [19, 18, 17]  # 변경할 막대 인덱스 (0부터 시작)
for i in change_color_indices:
    bars[i].set_color('green')

# 상위 3개 막대에 민원건수 표시 (백만 단위)
for i in range(3):
    x = bars[-(i+1)].get_width()
    y = bars[-(i+1)].get_y() + bars[-(i+1)].get_height()/2
    value = x / 1000000  # 백만 단위로 변환
    ax.text(x + (x * 0.02), y, 
            f'{value:.2f}M', 
            va='center', ha='left', fontweight='bold')

ax.set_xlabel('민원건수(단위:백만건)')
ax.set_title('2022년 기준 키워드 기반 민원 현황(상위 20개)')

# y축 라벨을 상단에 수평으로 표시
ax.text(-0.003, 1.0012, '<민원내용>', transform=ax.transAxes, ha='right', va='bottom', rotation=0)

# x축 범위 조정 (필요한 경우)
ax.set_xlim(0, ax.get_xlim()[1] * 1.05)  # x축 최대값 증가

# 상단선과 우측선의 모양을 점선으로 설정
ax.spines['top'].set_linestyle('--')
ax.spines['top'].set_linewidth(0.5)
ax.spines['right'].set_linestyle('--')
ax.spines['right'].set_linewidth(0.5)

plt.xlabel('민원건수(단위:백만건)')
# plt.ylabel('민원내용')
plt.title('2022년 기준 키워드 기반 민원 현황(상위 20개)')
plt.tight_layout()
plt.savefig('민원건수20.png', dpi=300)
plt.show()


#%%
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 한글 폰트 경로 설정
font_path = "C:/Users/Charlie/AppData/Local/Microsoft/Windows/Fonts/경기천년제목_Medium.ttf"

# 워드클라우드 객체 생성 (외곽선 제거 위해 contour_width=0 설정)
wordcloud = WordCloud(font_path=font_path, background_color='white', width=800, height=600, contour_width=0)

# '민원내용'을 키로, '민원건수'를 값으로 하는 딕셔너리 생성
word_freq = {x[0]:x[1] for x in df[['민원내용', '민원건수']].values}

# 워드클라우드 생성
wordcloud = wordcloud.generate_from_frequencies(word_freq)

# 워드클라우드 시각화
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # 축 표시 제거
plt.savefig('워드클라우드.png', dpi=300)
plt.show()


