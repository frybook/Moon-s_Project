#%% excel일경우 불러오기
import pandas as pd 

folder = 'C:/Python/pandas/pyscraping-main/data/ch05/'
excel = folder +"CES마켓_주문내역.xlsx"
df = pd.read_excel(excel)


# df = pd.read_excel('C:/Python/pandas/pyscraping-main/data/ch05/CES마켓_주문내역.xlsx')

#%% csv일 경우 불러오기

import pandas as pd

folder = 'C:/Python/pandas/pyscraping-main/data/ch05/'
excel2 = folder + "A_product_sales.csv"

dx = pd.read_csv(excel2)

dx2 = pd.read_csv(excel2,index_col="연도") # 인덱스 프레임 바꾸기
#%%
# 폴더에 저장하기
# dx2.to_csv("저장") 현재 폴더 지정
dx2.to_csv('C:/Python/pandas/pyscraping-main/data/ch05/저장') # 주소지정
#%%
import pandas as pd

# 엑셀로 저장하기
df.to_excel("test.xlsx")

# 엑셀파일 읽기
df = pd.read_excel("test.xlsx")

