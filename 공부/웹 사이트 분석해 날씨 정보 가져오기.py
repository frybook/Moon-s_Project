# 웹사이트 분석해 날씨 정보 가져오기

import requests
from bs4 import BeautifulSoup

location = "서울시 종로구 청운동"

search_query = location + "날씨"
search_url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q="
url = search_url + search_query

html_weather = requests.get(url).text
soup_weather = BeautifulSoup(html_weather,"lxml")
print(url)

#%%
txt_temp = soup_weather.select_one('strong.txt_temp').get_text()
print(txt_temp) # 15℃

#%%
txt_weather = soup_weather.select_one('span.txt_weather').get_text()
print(txt_weather)

#%%
dl_weather_dds = soup_weather.select('dl.dl_weather dd')
dl_weather_dds

#%%

[wind_speed,humidity,pm10] = [x.get_text() for x in dl_weather_dds]
# 순서대로 텍스트 가져오기
print(f"현재풍속  : {wind_speed}, 현재 습도 : {humidity} , 미세 먼지 : {pm10}")

#%%
import requests
from bs4 import BeautifulSoup
import time
# BeautifulSoup(html_weather, "lxml")
def get_weather_daum(location):
    search_query = location + "날씨"
    search_url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q="
    url = search_url + search_query
    html_weather = requests.get(url).text
    time.sleep(2)
    soup_weather = BeautifulSoup(html_weather, "lxml")
    
    txt_temp = soup_weather.select_one('strong.txt_temp').get_text()
    txt_weather = soup_weather.select_one('span.txt_weather').get_text()
    
    dl_weather_dds = soup_weather.select("dl.dl_weather dd")
    [wind_speed,humidity,pm10] = [x.get_text() for x in dl_weather_dds]
    
    return (txt_temp, txt_weather , wind_speed, humidity,pm10)

#%%
location = "서울시 종로구 청운동"
get_weather_daum(location)

#%%

location = "경기도 수원시"

(txt_temp, txt_weather, wind_speed ,humidity, pm10) = get_weather_daum(location)

print("----[오늘의 날씨 정보](Daum)----")
print(f"설정 지역: {location}")
print(f"기온 : {txt_temp}")
print(f"날씨 정보: {txt_weather}",)
print(f"현재 풍속 : {wind_speed},현재 습도 : {humidity}, 미세 먼지 : {pm10}")

#%%
import schedule
import time
from datetime import datetime

def job():
    now = datetime.now()
    print("[작업 수행 시각]{:%H:%M:%S}".format(now))
    location = "경기도 수원시"
    
    (txt_temp, txt_weather, wind_speed ,humidity, pm10) = get_weather_daum(location)
    
    print("----[오늘의 날씨 정보](Daum)----")
    print(f"설정 지역: {location}")
    print(f"기온 : {txt_temp}")
    print(f"날씨 정보: {txt_weather}",)
    print(f"현재 풍속 : {wind_speed},현재 습도 : {humidity}, 미세 먼지 : {pm10}")
    
schedule.every(5).seconds.do(job)

while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except:
        print("작업 강제 종료")
        schedule.clear()
        break