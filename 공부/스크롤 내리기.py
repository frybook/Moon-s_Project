# 스크롤 내리기
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
print("최대화된 창의 크기 및 위치:", driver.get_window_position(), driver.get_window_size())
driver.quit()
# 최대화된 창의 크기 및 위치: {'x': -8, 'y': -8} {'width': 1936, 'height': 1056}
# {왼쪽 상단 모퉁이의 x좌표, y: 오른쪽 상단 모통이의 y좌표} {창의 너비와 높이}
window_size = {'width': 1936, 'height': 1056}
half_width = window_size['width'] // 2
# 절반크기로 브라우저 크기 축소시켜서 web_scroll 구현
print("절반 크기:", half_width)
#%%
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup 
def web_scroll(url):
    options = Options() # 옵션 추가를 위한 준비
    options.headless = False  #  Chrome 브라우저를 화면에 표시할지 여부 
    # False로 설정되어 있으므로, 브라우저가 화면
    options.add_argument('--window-size=968,1056') # 절반크기 화면 
    driver = webdriver.Chrome(options=options) # 디버깅할때 여긴 수정 **
    time.sleep(3) # 웹 로드
    step = 0.9 #웹 페이지의 90%만큼 이동
    scroll = 8 # 총 8번이 스크롤 될 동안 실행
    screen_size = driver.execute_script("return window.screen.height;") # 1056pixel 창높이 설정
    while scroll> 0:
        driver.execute_script("window.scrollTo(0,{screen_height}*{step})".format(screen_height=screen_size, step=step))
        step += 0.9
        step+= 0.9
        time.sleep(3) 
        scroll -= 1
    driver.get(url)     
    html_text = driver.page_source #웹페이지의 소스코드(html) python에 가져오기  
    soup = BeautifulSoup(html_text,'lxml') # lxml 파서는 큰 html문서처리에 용이(반면에 html_parser는 간단한 문서처리에 활용)
    return soup
