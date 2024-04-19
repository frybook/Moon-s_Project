import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.options import Options
#%%
# 검색어
# info = input("검색할 내용을 말해주세요 : ")
info = input("검색할 내용을 말해주세요 : ")
translation = "한글로 번역"
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
new_summary = []

for i in urls:
    driver.get(i)
    time.sleep(4)
    driver.find_element(By.ID, "yt_ai_summary_header_toggle").click()    
    driver.find_element(By.ID, "yt_ai_summary_header_summary").click()
    
    # summary 버튼 클릭
    time.sleep(4)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(5)
    # driver.send_keys(Keys.ENTER)
    # 진행하다 보면 내용이 긴 작업은 아래 내려가는 버튼으로 스크롤을 내릴 필요가 있다.
    try:# 내용이 길 경우 버튼 클릭이 필요
        downscoll = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/main/div[2]/div[1]/div/div/div/div/button').click()
        
    except:
        pass
    # 검색해서 나온 내용을 한글화
    GPT = driver.find_element(By.ID,'prompt-textarea')
    GPT.send_keys(translation)
    time.sleep(2)
    GPT.send_keys(Keys.ENTER)
    time.sleep(7)
    # 요약한 내용을 리스트로 만들고 다시 리스트화 시켜서 개별화 시킴
    html_A = driver.page_source
    chat = BeautifulSoup(html_A,'lxml')
    list_A = chat.select('div:nth-child(5) > div > div > div.relative.flex.w-full.flex-col.agent-turn > div.flex-col.gap-1.md\:gap-3 > div.flex.flex-grow.flex-col.max-w-full > div > div > ul > li')
    x = []
    for a in list_A:
        x.append(a.text)
    new_summary.append(x)
    driver.close() # 현재 창 종료
    driver.switch_to.window(driver.window_handles[-1])  #다시 이전 창(탭)이동 그래야 설정이 계속 적용됌
    time.sleep(1)
#%%
# 새탭으로 이동
pd = pd.DataFrame(new_summary) 
pd.to_csv(info + ".csv")
pd.to_excel(info + ".xlsx")
#%%
'''
- 새로 열은 탭으로 이동
- 새 탭에서 버튼 이용
- 새탭 종료
- 다시 처음 탭으로 설정해서 작업 진행

- 요약이 많은 경우도 있을수있음으로 확인하고 추가 작업
- 유튜브 내용중에 필요한 내용만 나오도록 중간에 내 추천 영상 같은게 껴있음(추천영상은 해결 방법이 없음)

'''
# 현재 문제
# 새탭을 여는 프로그램이 글자로 변경을하지 못하면 먹통이되는 문제가 있음
# 그래서 단축키를 하나 더 넣고 다시 클릭한뒤에 엔터까지 치는 걸 넣는다.
# (작업에 클릭,엔터 추가로 해결)
# 쇼츠 영상에서 
