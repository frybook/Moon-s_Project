import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.options import Options
from datetime import datetime
#%%
# 검색어
# info = input("검색할 내용을 말해주세요 : ")
info = "뮤지컬"

# 디버그 구글로그인된 크롬을 준비
chrome_options = Options() ## 옵션 추가를 위한 준비
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222") ## 디버깅 옵션 추가
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(3)
#%%
# 검색한 여러 영상에 urls,titles 정보값을 얻음
# 주소
driver.get("https://www.youtube.com/")

# 검색창 찾기
youtube = driver.find_element(By.NAME,'search_query')
# 검색어 입력
youtube.send_keys(info)
time.sleep(2)
# 검색
youtube.send_keys(Keys.ENTER)
time.sleep(2)

if(True):
    y = 0
    y_step = 3000
    for k in range(1,3):
        y = y + y_step
        script = "window.scrollTo({0},{1})".format(0,y)
        driver.execute_script(script)
        time.sleep(3)

html = driver.page_source

soup = BeautifulSoup(html,'lxml') # 가져온 html을 lxml로 html문서로 변환

title = soup.select('a#video-title') # a태그에서 select 해서 

titles = []
urls = []
for tag in title:
    name = tag['title']
    url = tag['href']
    titles.append(name)
    urls.append("https://www.youtube.com"+ url)
#%%
# 반복문으로 url에 들어가서 summary요약을 저장
relist = []
for i in urls:
    driver.get(i)
    time.sleep(4)
    summary = driver.find_element(By.ID, "yt_ai_summary_header_summary").click()
    time.sleep(4)




#%%
'''
창을 여는데까진 성공(2024.04.17)
이제 열린 새 창으로 넘어가고 
그다음에 요약된 내용을 데이터 프레임화 시켜야된다.
(html로 만들어서 가져온뒤에)'''


//*[@id="__next"]/div[1]/div[2]/main/div[2]/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div/ul/li[1]/font
//*[@id="__next"]/div[1]/div[2]/main/div[2]/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div/ul/li[1]/font/font
//*[@id="__next"]/div[1]/div[2]/main/div[2]/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div/ul/li[2]/font
//*[@id="__next"]/div[1]/div[2]/main/div[2]/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div/ul/li[2]/font/font
//*[@id="__next"]/div[1]/div[2]/main/div[2]/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div/ul/li[3]/font
//*[@id="__next"]/div[1]/div[2]/main/div[2]/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div/ul/li[3]/font/font