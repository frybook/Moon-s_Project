import pyautogui

# 현재 사용하는 모니터의 해상도 출력
print(pyautogui.size())

# 현재 마우스 커서의 위치 출력
print(pyautogui.position())

pyautogui.mouseInfo() # 좌표 색깔 확인

pyautogui.moveTo(100, 100) 
# pyautogui.click(clicks=2, interval=0.2, button='right')
pyautogui.click(960,540, interval=0.2, button='right') # 좌표 설정 우클릭

# 스크롤 내리기
pyautogui.scroll(-100) # 아래
pyautogui.scroll(100)  # 위
# 마우스 클릭
pyautogui.click()
pyautogui.click(button='right')
pyautogui.doubleClick()
pyautogui.click(clicks=3, interval=1) 
# interval 속도
# 사람처럼 보이게 시간을 랜덤으로 줌
import time
import random
time.sleep( random.uniform(2,4))


