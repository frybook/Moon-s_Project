import os
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 저장 경로
current_path = os.getcwd()
# 원하는 검색어 및 이미지 개수
inserturl = input("폴더 명 : ").strip()
img_num = input("원하는 이미지 개수 입력하세요 : ").strip()
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://www.google.com")
# driver.maximize_window()
# # 복수 이미지 정보를 가져옵니다 list 형  * find_elements 를 사용합니다.
# images = driver.find_elements(By.CSS_SELECTOR, ".thumb_img")
# 폴더 명도 검색어랑 동일하게 세팅 !
folder_name = inserturl
# 폴더 있는지 없는지 확인 후 생성
if not os.path.isdir(folder_name):
    os.mkdir(folder_name)
# 원하는 개수의 이미지만 다운로드!
img_count = 1
while True:
    try: # 복수 이미지 정보를 가져옵니다 list 형  * find_elements 를 사용합니다.
        images = driver.find_elements(By.CSS_SELECTOR, ".thumb_img")
        if img_count > int(img_num):# 입력한 값
            break
        else:
            try:# 이미지 다운에 중요한 src 값 가져오기
                img_url = images.get_attribute('src')
                time.sleep(1)
                # URL 열기를 위한 확장 가능한 라이브러리
                urllib.request.urlretrieve(img_url, folder_name + "/" + inserturl + "." + str(img_count) + ".jpg")
                img_count += 1
                # 다음으로 넘기기
                driver.find_element(By.CSS_SELECTOR,"").click()
            except:
                print("error")
                pass
    except:
        print("겉에 오류")
        pass