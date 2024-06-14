
import cv2
import os

def threshold(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (2000, 3000))
    ret, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    return image


# 1. 보표 영역 추출 및 그 외 노이즈 제거
def playing(image):
    image = threshold(image)  # 이미지 이진화
    cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(image)  # 레이블링
    for i in range(1, cnt):
        x, y, w, h, area = stats[i]
        if w > image.shape[1] * 0.5:  # 작은 블럭은 제외시키기 위해
            h = int(h * 1.2) 
            cv2.rectangle(image, (x, y + int(h * 0.2), w, h), (240, 0, 0), -1)
    # 색 전환        
    image = cv2.bitwise_not(image)
    
    # 이미지화
    output_filename = (f"img_{number}.png")
    cv2.imwrite(output_filename, image)

# 이미지 불러오기
number = 1
while True:
    try: 
       image = cv2.imread(f"page_{number}.png")
       playing(image)
       number += 1
       
    except:
       print("멈춤")
       break


    

