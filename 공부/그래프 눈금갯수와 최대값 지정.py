import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#%%
data = {'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data)
df.plot()
plt.gca().yaxis.set_major_locator(ticker.MaxNLocator())
'''
plt.gca() 현재 축 가져오기
yaxis 가져올 축 지정
ticker.MaxNLocator(nbins=10) ticker 모듈에서 MaxNLocator 객체를 생성합니다
nbins=10 축에 눈금 갯수 지정
'''
plt.show()
#%%  축에 최대 값 증가
data = {'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data)
df.plot()
plt.ylim(3, 10)  # y축에 최대 값 증가
plt.show()
