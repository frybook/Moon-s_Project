
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
# 검색어
info = input("검색할 내용을 말해주세요 : ")
# 주소
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
# 검색창 찾기
youtube = driver.find_element(By.NAME,'search_query')
# 검색어 입력
youtube.send_keys(info)
time.sleep(2)
# 검색
youtube.send_keys(Keys.ENTER)
time.sleep(2)

# 필터창 열기
driver.find_element(By.XPATH, '//*[@id="filter-button"]').click()
time.sleep(1)
# 이번주 필터 선택
# 이번주에서 id endpoint 클릭
# options = driver.find_element(By.XPATH,'//*[@id="options"]/ytd-search-filter-group-renderer[1]/ytd-search-filter-renderer[3]')
# options.find_element(By.ID , "endpoint").click() 
# time.sleep(2)
# 다시 필터창열기
# driver.find_element(By.XPATH, '//*[@id="filter-button"]').click()
# time.sleep(1)
# 조회수 필터 선택
click_list = driver.find_element(By.XPATH,'//*[@id="options"]/ytd-search-filter-group-renderer[5]/ytd-search-filter-renderer[3]')
click_list.find_element(By.ID , "endpoint").click()
time.sleep(2)


# # 스크롤을 화면 가장 아래로 내린다
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# # 페이지 로딩 대기
# time.sleep(2)


# 스크롤 내리기
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
        
# 동영상 제목과 URL추출하기
title = soup.select('a#video-title') # a태그에서 select 해서 

titles = []
urls = []
for tag in title:
    name = tag['title']
    url = tag['href']
    titles.append(name)
    urls.append("https://www.youtube.com"+ url)
# 조회수와 업로드 시기 추출하기

view_numbers  = soup.select('#metadata-line > span:nth-child(3)')
upload_times = soup.select('#metadata-line > span:nth-child(4)')


# view_uploads = soup.select('span.style-scope.ytd-video-meta-block')
# view_numbers = view_uploads[0::2]
# upload_times = view_uploads[1::2]

views = []
uploads = []
for view_number,upload_time in zip(view_numbers,upload_times):
    view = view_number.get_text().split(" ")[-1] # "조회수 --만회에서 _기준으로 나누고 뒤에서 1인  -1 값만 불러옴
    upload = upload_time.get_text()
    views.append(view)
    uploads.append(upload)
    
# 추출된 정보 모으기
search = []
for title,url,view,upload in zip(titles,urls,views,uploads):
    searchs = [title,url,view,upload]
    search.append(searchs)

# 추출 결과를 판다스 데이터프레임 형식으로 변환
df = pd.DataFrame(search,columns=["제목","링크","조회수","업로드"])

df.to_csv(info + ".csv")
df.to_excel(info + ".xlsx")

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd

# 검색어
info = input("검색할 내용을 말해주세요 : ")
# 주소
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
# 검색창 찾기
youtube = driver.find_element(By.NAME,'search_query')
# 검색어 입력
youtube.send_keys(info)
time.sleep(2)
# 검색
youtube.send_keys(Keys.ENTER)
time.sleep(2)

# 필터창 열기
driver.find_element(By.XPATH, '//*[@id="filter-button"]').click()
time.sleep(1)
# 이번주 필터 선택
# 이번주에서 id endpoint 클릭
# options = driver.find_element(By.XPATH,'//*[@id="options"]/ytd-search-filter-group-renderer[1]/ytd-search-filter-renderer[3]')
# options.find_element(By.ID , "endpoint").click() 
# time.sleep(2)
# 다시 필터창열기
# driver.find_element(By.XPATH, '//*[@id="filter-button"]').click()
# time.sleep(1)
# 조회수 필터 선택
click_list = driver.find_element(By.XPATH,'//*[@id="options"]/ytd-search-filter-group-renderer[5]/ytd-search-filter-renderer[3]')
click_list.find_element(By.ID , "endpoint").click()
time.sleep(2)


# # 스크롤을 화면 가장 아래로 내린다
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# # 페이지 로딩 대기
# time.sleep(2)

#%%
# 스크롤 내리기
if(True):
    y = 0
    y_step = 3000
    for k in range(1,3):
        y = y + y_step
        script = "window.scrollTo({0},{1})".format(0,y)
        driver.execute_script(script)
        time.sleep(3)

#%%
html = driver.page_source

soup = BeautifulSoup(html,'lxml') # 가져온 html을 lxml로 html문서로 변환
        
# 동영상 제목과 URL추출하기
title = soup.select('a#video-title') # a태그에서 select 해서 

titles = []
urls = []
for tag in title:
    name = tag['title']
    url = tag['href']
    titles.append(name)
    urls.append("https://www.youtube.com"+ url)
# 조회수와 업로드 시기 추출하기

view_numbers  = soup.select('#metadata-line > span:nth-child(3)')
upload_times = soup.select('#metadata-line > span:nth-child(4)')


# view_uploads = soup.select('span.style-scope.ytd-video-meta-block')
# view_numbers = view_uploads[0::2]
# upload_times = view_uploads[1::2]

views = []
uploads = []
for view_number,upload_time in zip(view_numbers,upload_times):
    view = view_number.get_text().split(" ")[-1] # "조회수 --만회에서 _기준으로 나누고 뒤에서 1인  -1 값만 불러옴
    upload = upload_time.get_text()
    views.append(view)
    uploads.append(upload)
    
# 추출된 정보 모으기
search = []
for title,url,view,upload in zip(titles,urls,views,uploads):
    searchs = [title,url,view,upload]
    search.append(searchs)

# 추출 결과를 판다스 데이터프레임 형식으로 변환
df = pd.DataFrame(search,columns=["제목","링크","조회수","업로드"])

df.to_csv(info + ".csv", encoding ='cp949')
df.to_excel(info + ".xlsx")

#,encoding="CP949"