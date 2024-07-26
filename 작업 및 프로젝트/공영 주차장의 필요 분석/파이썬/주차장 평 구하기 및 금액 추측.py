'''
출입구가 1개일 경우
직각
일반형 너비 2.5 x 5 x 0.3025 = 3.78125평 (주차 구획만)
주차로 너비 6 * 0.3025 = 1.815평 (차를 뺄 공간)
45도 대향 주차일 경우 5 * 0.3025 = 1.5125평 ()

일반일 경우 5.59평
45도 대향 일 경우 5.29평
'''
#%%

import pandas as pd

df = pd.read_excel("수원시주차창정보표준데이터.xlsx", index_col=None)
Paldal_gu_df = df[df['소재지지번주소'].str.contains('팔달구', na=False)]
Paldal_gu_df = Paldal_gu_df[Paldal_gu_df['주차장유형'].str.contains('노외', na=False)]


#%%
import pandas as pd
df = pd.read_excel("불법주차_건수.xlsx")
#%%
df= pd.read_csv("경기도_수원시_주정차단속현황_20240122.CSV", encoding='euc-kr')
df1= pd.read_csv("경기도_수원시_주정차단속현황_20221227.csv", encoding='euc-kr')
pdf = pd.concat([df, df1])
pdf['단속건수'] = pdf['단속건수'].str.replace(',', '').astype(int)
#%%
# 건수와 주차자리 비례
Paldal_gu_df = pdf[pdf['시군구명'].str.contains('팔달구청', na=False)]
Paldal_gu_sum = Paldal_gu_df.groupby('단속동')['단속건수'].sum().reset_index()
Yeongtong_gu_df = pdf[pdf['시군구명'].str.contains('영통구청', na=False)]
Yeongtong_gu_sum = Yeongtong_gu_df.groupby('단속동')['단속건수'].sum().reset_index()
print(Paldal_gu_sum)
#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False
import matplotlib.font_manager as fm
#%% 폰트위치
font_files = fm.findSystemFonts(fontpaths=['C:/Users/moon/AppData/Local/Microsoft/Windows/Fonts'])
for fpath in font_files:
    fm.fontManager.addfont(fpath)
    
    
#%%
# 팔달구
plt.figure(figsize=(15, 8))
plt.bar(Paldal_gu_sum['단속동'], Paldal_gu_sum['단속건수'], color='blue')

# Customize the plot
plt.xlabel('단속동')
plt.ylabel('단속건수')
plt.title('팔달구에 단속동과 단속건수')
plt.xticks(rotation=45)  

# Display the plot
plt.tight_layout()
plt.show()

#%%
plt.figure(figsize=(15, 8))
plt.bar(Yeongtong_gu_sum['단속동'], Yeongtong_gu_sum['단속건수'], color='blue')

# Customize the plot
plt.xlabel('단속동')
plt.ylabel('단속건수')
plt.title('영통구에 단속동과 단속건수')
plt.xticks(rotation=45)  

# Display the plot
plt.tight_layout()
plt.show()

#%%
'''
구로구는 2018년부터 거리공원 지하 공간을 활용해 연면적 7313㎡, 
총 202면(지하 1층 98면ㆍ지하 2층 104면)의 주차장 건설을 추진해 왔다. 
지하주차장 관련 예상 사업비는 약 230억원이다.
'''