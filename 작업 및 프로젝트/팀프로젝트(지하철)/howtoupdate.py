# -*- coding: utf-8 -*-
import os
os.system('pip install --upgrade selenium')

# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver

# selenium으로 무엇인가 입력하기 위한 import
from selenium.webdriver.common.keys import Keys

# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time

# selenium 버전 확인하기
print(webdriver.__version__)  # 4.19.0

# 크롤링한 싸이트 주소
url = "https://naver.com"

# 크롬드라이버 실행
driver = webdriver.Chrome()

# 크롬드라이버로 싸이트 불러오기
driver.get(url)

# 페이지가 완전히 로딩되도록 3초동안 기다림
time.sleep(3)

# # 네이버 로그인 버튼 xpath
# xpath = '//*[@id="account"]/div/a'

# # 네이버 로그인 버튼 클릭 
# driver.find_element("xpath", xpath).click()

# 네이버 검색창에 '서울 지하철 혼잡' 검색하기
xpath = '//*[@id="query"]'
text ='서울 지하철 혼잡'

# 네이버 검색창에 검색어 타이핑 
driver.find_element("xpath", xpath).send_keys(text)

# 네이버 검색창에 검색어 클릭하기 
xpath = '//*[@id="search-btn"]'
driver.find_element("xpath", xpath).click()

## selenium 최신 버전 항상 설치하는 방법임
# 출처 : https://youtu.be/Mw2modVN-II?si=Dn5xWRpNS1oejgmh

## selenium으로 버튼 클릭, 검색창에 검색어 넣고 검색버튼 클릭 자동화
# 출처 : https://youtu.be/E_ETtfTvjPk?si=eqB7YEGXQgc_MiZ9

