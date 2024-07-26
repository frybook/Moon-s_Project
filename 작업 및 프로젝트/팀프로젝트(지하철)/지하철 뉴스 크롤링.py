from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time


#%%
#분석 배경
driver = webdriver.Chrome()
driver.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=news&ssc=tab.news.all&query=%EC%A7%80%ED%95%98%EC%B2%A0+%ED%98%BC%EC%9E%A1&oquery=%EC%A7%80%ED%95%98%EC%B2%A0&tqi=imAbAdqo1awsssxaLiRssssst58-117659")
time.sleep(2)


if(True):
    y = 0
    y_step = 3000
    for k in range(0,6):
        y = y + y_step
        script = "window.scrollTo({0},{1})".format(0,y)
        driver.execute_script(script)
        time.sleep(3)

# 페이지 소스 가져오기
html = driver.page_source
# html화
soup = BeautifulSoup(html,'lxml')
#%%
# 제목
titles = []
title = soup.select('a.news_tit')
for tag in title:
    name = tag['title']
    titles.append(name)

#%%
df = pd.DataFrame(titles,columns=["기사제목"])
df.to_csv('기사제목' + ".csv",index=False)
