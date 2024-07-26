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

df['비례'] = ((df['주차공간'] - df['자동차수']) / df['자동차수']) * 100

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Bar width
bar_width = 0.35

# Set position of bar on X axis
r1 = range(len(df))
r2 = [x + bar_width for x in r1]

# Plot bars for '자동차수' (Total Cars)
bars1 = ax.bar(r1, df['자동차수'], width=bar_width, color='b', alpha=0.6, label='자동차수')

# Plot bars for '주차공간' (Number of public parking lots)
bars2 = ax.bar(r2, df['주차공간'], width=bar_width, color='g', alpha=0.6, label='주차공간')

# Adding labels and title
ax.set_xlabel('기준')
ax.set_ylabel('자동차수')
plt.title('자동차수와 주차공간')

# Adding percentage difference as annotations on bars
for i, (bar1, bar2) in enumerate(zip(bars1, bars2)):
    height1 = bar1.get_height()
    height2 = bar2.get_height()
    percentage_diff = df.loc[i, '비례']
    ax.text(bar1.get_x() + bar1.get_width() / 2, height1 + 10, f'{percentage_diff:.1f}%', ha='center', va='bottom', fontsize=10)

# Adding x-axis ticks
plt.xticks([r + bar_width / 2 for r in r1], df['기준'])

# Adding legends
ax.legend()

# Show plot
plt.tight_layout()
plt.show()