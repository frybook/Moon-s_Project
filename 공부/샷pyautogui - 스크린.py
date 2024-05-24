import pyautogui

im1 = pyautogui.screenshot()
im2 = pyautogui.screenshot('my_screenshot.png') # my_screenshot.png 이름으로 저장

# 왼쪽 위쪽 너비 높이 순으로 세팅
im = pyautogui.screenshot(region=(0,0, 300, 400))


import pyautogui as p

dest = "C:/Users/root/Desktop/"

p.screenshot()  #전체 화면 스크린샷 찍고 이미지 객체로 전달
p.screenshot(dest +"all.jpg") #전체 화면 스크린샷 찍고 파일로 저장
p.screenshot(region=(0, 0, 100, 100)) #지정영역 스크린샷 찍고 이미지 객체로 전달
p.screenshot(dest +"part.jpg", region=(0, 0, 100, 100)) #지정영역 스크린샷 찍고 파일로 저장