import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_excel("주차장,인구,단속,자동차등록,총합.xlsx", index_col=None)
df['주차공간'] = df['공영주차장'] + df['건물주차장'] + df['거주자우선']

#%%
import matplotlib as mpl
mpl.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False
import matplotlib.font_manager as fm
#%% 폰트위치
font_files = fm.findSystemFonts(fontpaths=['C:/Users/moon/AppData/Local/Microsoft/Windows/Fonts'])
for fpath in font_files:
    fm.fontManager.addfont(fpath)
    
fig, ax = plt.subplots(figsize=(12, 8))

df = df.loc[4]
print(df)
#%%
import matplotlib.pyplot as plt

# Given data
public_parking = 8807
building_parking = 366437
resident_priority_parking = 17764
total_parking_spaces = 393008

# Calculate the percentages
public_parking_pct = (public_parking / total_parking_spaces) * 100
building_parking_pct = (building_parking / total_parking_spaces) * 100
resident_priority_parking_pct = (resident_priority_parking / total_parking_spaces) * 100

# Data for the pie chart
labels = ['공영_주차장', '건물_주차장', '거주자_우선']
sizes = [public_parking_pct, building_parking_pct, resident_priority_parking_pct]
colors = ['#ff9999','#66b3ff','#99ff99']
explode = (0.1, 0, 0)  # explode the 1st slice (i.e. 'Public Parking')

# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=140)
plt.title('유형별 주차공간 비율')

# Add parking space numbers and total parking spaces in the upper right corner
text_str = (f"공영_주차장: {public_parking}\n"
            f"건물_주차장: {building_parking}\n"
            f"거주자_우선: {resident_priority_parking}\n"
            f"총_주차_가능수: {total_parking_spaces}")
plt.text(1.1, 1, text_str, transform=plt.gca().transAxes, verticalalignment='top')

plt.show()