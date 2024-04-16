<<<<<<< HEAD
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


# 디버그 구글로그인된 크롬을 준비
chrome_options = Options() ## 옵션 추가를 위한 준비
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222") ## 디버깅 옵션 추가
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(3)

# 유튜브 한국 인기곡 TOP100
url = "https://music.youtube.com/playlist?list=PL4fGSI1pDJn6jXS_Tv_N9B8Z0HTRVJE0m"
driver.get(url)

# html 문서화
html = driver.page_source
soup = BeautifulSoup(html,'lxml') 

# 
title = soup.select("div.flex-columns.style-scope.ytmusic-responsive-list-item-renderer > div.title-column.style-scope.ytmusic-responsive-list-item-renderer > yt-formatted-string > a")
urls_tag = []
for tag in title:
    url = tag['href']
    urls_tag.append("https://music.youtube.com/"+ url)
    
# urls_tag에 노래링크,가수링크,앨범링크 순으로 짤라야됌

# 노래 제목
title = soup.select("div.title-column.style-scope.ytmusic-responsive-list-item-renderer > yt-formatted-string")
urls_name = []
for name in title:
    info = name['title']
    urls_name.append(info)
    
# 가수, 앨범명
singer  = soup.select('div.secondary-flex-columns.style-scope.ytmusic-responsive-list-item-renderer > yt-formatted-string:nth-child(1)')
album = soup.select('div.secondary-flex-columns.style-scope.ytmusic-responsive-list-item-renderer > yt-formatted-string:nth-child(2)')

singer_name = []
album_name = []
for a,b in zip(singer,album):
    human = a.get_text()
    album_code = b.get_text()
    singer_name.append(human)
    album_name.append(album_code) 
#%%

# 추출한 정보 한곳으로 모으기
search = []
for title,name,url,code in zip(urls_name,singer_name,urls_tag,album_name):
    searchs = [title,name,url,code]
    search.append(searchs)
    
# 데이터 프레임으로 변환

df = pd.DataFrame(search,columns=["곡","가수","링크","앨범"])
today = datetime.today().date()
df.to_csv("인기TOP100" + "_" + f'{today}' + ".csv")
df.to_excel("인기TOP100" + "_" + f'{today}'  + ".xlsx")
=======
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from IPython.display import HTML


# 디버그 구글로그인된 크롬을 준비
chrome_options = Options() ## 옵션 추가를 위한 준비
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222") ## 디버깅 옵션 추가
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(3)

# 유튜브 한국 인기곡 TOP100
url = "https://music.youtube.com/playlist?list=PL4fGSI1pDJn6jXS_Tv_N9B8Z0HTRVJE0m"
driver.get(url)

# html 문서화
html = driver.page_source
soup = BeautifulSoup(html,'lxml') 

# 
title = soup.select("div.flex-columns.style-scope.ytmusic-responsive-list-item-renderer > div.title-column.style-scope.ytmusic-responsive-list-item-renderer > yt-formatted-string > a")
urls_tag = []
for tag in title:
    url = tag['href']
    urls_tag.append("https://music.youtube.com/"+ url)
    
# urls_tag에 노래링크,가수링크,앨범링크 순으로 짤라야됌

# 노래 제목
title = soup.select("div.title-column.style-scope.ytmusic-responsive-list-item-renderer > yt-formatted-string")
urls_name = []
for name in title:
    info = name['title']
    urls_name.append(info)
    
# 가수, 앨범명
singer  = soup.select('div.secondary-flex-columns.style-scope.ytmusic-responsive-list-item-renderer > yt-formatted-string:nth-child(1)')
album = soup.select('div.secondary-flex-columns.style-scope.ytmusic-responsive-list-item-renderer > yt-formatted-string:nth-child(2)')

singer_name = []
album_name = []
for a,b in zip(singer,album):
    human = a.get_text()
    album_code = b.get_text()
    singer_name.append(human)
    album_name.append(album_code) 
#%%

# 추출한 정보 한곳으로 모으기
search = []
for title,name,url,code in zip(urls_name,singer_name,urls_tag,album_name):
    searchs = [title,name,url,code]
    search.append(searchs)
    
# 데이터 프레임으로 변환

df = pd.DataFrame(search,columns=["곡","가수","링크","앨범"])
# df.index = df.index+1
# df.index.name = '순위'
df_rank = pd.DataFrame({'순위': range(1, len(df.index) + 1)})
df = pd.concat([df_rank,df], axis=1)

today = datetime.today().date()
df.to_csv("인기TOP100" + "_" + f'{today}' + ".csv")
df.to_excel("인기TOP100" + "_" + f'{today}'  + ".xlsx")

#%%
# 데이터프레임을 HTML로 변환
df_html = df.to_html(index = False,classes='table table-striped')
# index = False
print(df_html)
#%%

html_code = '''
<!DOCTYPE hrml>
<html>
    <head>
        <title>유튜브 뮤직 TOP100</title>
    </head>
    <body>
    <h1> 유튜브 뮤직 TOP100 <h1>
    <h3> * 업데이트 날짜 : {0:%Y-%m-%d}<h3>
        {1}
    <body>
</html>
'''.format(today,df_html)

#%% 생성할 HTML 파일 이름 지정
file_name = f"C:\Python\Syntex\따로 공부\유튜브 뮤직 인기TOP100 - {today}.html"

with open(file_name, 'w', encoding= "utf-8")as f:
    f.write(html_code)
    
print("생성자 파일: ",file_name)

>>>>>>> main
