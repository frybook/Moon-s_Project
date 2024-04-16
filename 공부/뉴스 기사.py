<<<<<<< HEAD
import feedparser

query = "머신러닝"

rss_url = f'https://news.google.com/rss/search?q={query}&hl=ko&gl=KR&ceid=KR%3Ako'
rss_news = feedparser.parse(rss_url)


title = rss_news['feed']['title']
updated = rss_news['feed']['updated']

print("[구글 뉴스 'RSS 피드 제목']",title)
print("[구글 뉴스 ' RSS 피드 제공 일시']",updated)

from datetime import datetime, timedelta

# RSS 피드 제공 일시를 한국 날짜와 시간으로 변경

def get_local_datetime(rss_datetime):
    # 전체 값 중에서 날짜와 시간만 문자열로 추출
    date_time_str = ' '.join(rss_datetime.split()[1:5])
    # 구분자 _를 넣어줌으로  = Wed, 27 Mar 2024 00:43:08 GMT
    # 문자열의 각 자리에 의미를 부여해 datetime 객체로 변경
    date_time_GMT = datetime.strptime(date_time_str,"%d %b %Y %H:%M:%S")
        
    # GMT에 9시간을 더해 한국 시간대로 변경
    date_time_KST = date_time_GMT + timedelta(hours=9)
    
    return date_time_KST

print("['구글 뉴스' RSS피드 제공 일시]",get_local_datetime(updated))
#-----------------------------------------------------------------------------

# a = "Wed, 27 Mar 2024 00:43:08 GMT"
# B = ''.join(a.split()[1:5])
# print(B) # 27Mar202400:43:08
# "".join을 할 경우 뒤에서 나온 리스트값의 경계없이 합쳐져서 나옴
# "_".join인 경우에는 사이사이의 구분자(_)가 포함됌

#%%

import feedparser
import pandas as pd

df_gnews = pd.DataFrame(rss_news.entries) 
# 구글 뉴스에서.entries항목을 df로 변환

selected_columns = ["title","published","link"] # emtries안에 있는 열중에 관심있는거만
df_gnews2= df_gnews[selected_columns].copy() # 선택한 열만 다른 df로 복사

# published 열의 작성 일시를 한국 시간대로 변경

df_gnews2["published"] = df_gnews2['published'].apply(get_local_datetime)

df_gnews2.columns = ['제목','제공일시','링크'] # 열 이름 변경
df_gnews2.head(3)                              # 앞의 일부만 출력


#%%

from IPython.display import HTML

df = df_gnews2.head(5)

html_table = df.to_html(escape=False,render_links=True)
# df.to_html(escape=False,render_links=True)
# escape HTML 안전 시퀀스로 변환 안함
# render_links url을 html 링크로 변환
HTML(html_table)

#%%
from datetime import datetime,timedelta

google_news_datetime_KST = get_local_datetime(updated)

df = df_gnews2

html_table = df.to_html(justify='center',escape=False,render_links=True)
#
html_code = '''
<!DOCTYPE html>
<html>
  <head>
    <title>구글 뉴스 검색</title>
  </head>
  <body>
    <h1>{0}</h1>
    <h3> *검색 날짜 및 시각: {1}</h3>
    {2}
  </body>
</html>    
'''.format(title, google_news_datetime_KST, html_table)

file_name = "C:\Python\Syntex\따로 공부\기사.html"
with open(file_name, 'w', encoding="utf-8") as f:
    f.write(html_code)
    
print("생성한 파일:", file_name)


=======
import feedparser

query = "머신러닝"

rss_url = f'https://news.google.com/rss/search?q={query}&hl=ko&gl=KR&ceid=KR%3Ako'
rss_news = feedparser.parse(rss_url)


title = rss_news['feed']['title']
updated = rss_news['feed']['updated']

print("[구글 뉴스 'RSS 피드 제목']",title)
print("[구글 뉴스 ' RSS 피드 제공 일시']",updated)

from datetime import datetime, timedelta

# RSS 피드 제공 일시를 한국 날짜와 시간으로 변경

def get_local_datetime(rss_datetime):
    # 전체 값 중에서 날짜와 시간만 문자열로 추출
    date_time_str = ' '.join(rss_datetime.split()[1:5])
    # 구분자 _를 넣어줌으로  = Wed, 27 Mar 2024 00:43:08 GMT
    # 문자열의 각 자리에 의미를 부여해 datetime 객체로 변경
    date_time_GMT = datetime.strptime(date_time_str,"%d %b %Y %H:%M:%S")
        
    # GMT에 9시간을 더해 한국 시간대로 변경
    date_time_KST = date_time_GMT + timedelta(hours=9)
    
    return date_time_KST

print("['구글 뉴스' RSS피드 제공 일시]",get_local_datetime(updated))
#-----------------------------------------------------------------------------

# a = "Wed, 27 Mar 2024 00:43:08 GMT"
# B = ''.join(a.split()[1:5])
# print(B) # 27Mar202400:43:08
# "".join을 할 경우 뒤에서 나온 리스트값의 경계없이 합쳐져서 나옴
# "_".join인 경우에는 사이사이의 구분자(_)가 포함됌

#%%

import feedparser
import pandas as pd

df_gnews = pd.DataFrame(rss_news.entries) 
# 구글 뉴스에서.entries항목을 df로 변환

selected_columns = ["title","published","link"] # emtries안에 있는 열중에 관심있는거만
df_gnews2= df_gnews[selected_columns].copy() # 선택한 열만 다른 df로 복사

# published 열의 작성 일시를 한국 시간대로 변경

df_gnews2["published"] = df_gnews2['published'].apply(get_local_datetime)

df_gnews2.columns = ['제목','제공일시','링크'] # 열 이름 변경
df_gnews2.head(3)                              # 앞의 일부만 출력


#%%

from IPython.display import HTML

df = df_gnews2.head(5)

html_table = df.to_html(escape=False,render_links=True)
# df.to_html(escape=False,render_links=True)
# escape HTML 안전 시퀀스로 변환 안함
# render_links url을 html 링크로 변환
HTML(html_table)

#%%
from datetime import datetime,timedelta

google_news_datetime_KST = get_local_datetime(updated)

df = df_gnews2

html_table = df.to_html(justify='center',escape=False,render_links=True)
#
html_code = '''
<!DOCTYPE html>
<html>
  <head>
    <title>구글 뉴스 검색</title>
  </head>
  <body>
    <h1>{0}</h1>
    <h3> *검색 날짜 및 시각: {1}</h3>
    {2}
  </body>
</html>    
'''.format(title, google_news_datetime_KST, html_table)

file_name = "C:\Python\Syntex\따로 공부\기사.html"
with open(file_name, 'w', encoding="utf-8") as f:
    f.write(html_code)
    
print("생성한 파일:", file_name)


>>>>>>> main
