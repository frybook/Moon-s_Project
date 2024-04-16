# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

keyword = "여의도 베드타운"
result_list = []

# 페이지당 10개씩 검색
for page in range(1, 401):
    start = (page - 1) * 10 + 1
    url = f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query={keyword}&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=143&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={start}"
    res = requests.get(url)
    html = BeautifulSoup(res.text, "html.parser")
    news_items = html.select('.news_area')
    for item in news_items:
        date = item.select_one('.info_group').text.strip()  # 기사 작성 날짜
        title = item.select_one('.news_tit').text
        desc = item.select_one('.news_dsc').text
        link = item.select_one('.news_tit')['href']  # 링크 가져오기
        result_list.append({"Date": date, "Title": title, "Description": desc, "Link": link})

    btn_next = html.select_one('.btn_next')
    if 'href' not in btn_next.attrs:
        print('last page')
        break

df_web_search = pd.DataFrame(result_list)

# 링크를 클릭 가능한 형식으로 변경
df_web_search['Link'] = df_web_search['Link'].apply(lambda x: f'<a href="{x}">{x}</a>')  # 수정된 부분

html_table = df_web_search.head().to_html(escape=False, render_links=True)

now = datetime.datetime.now()

html_code = '''
<!DOCTYPE html>
<html>
  <head>
    <title>웹 문서 검색 결과</title>
  </head>
  <body>
    <h1> 웹 문서 검색 결과 (다음) </h1>
    <h3> * 데이터 추출 날짜: {0:%Y-%m-%d}</h3>
    {1}
  </body>
</html>
'''.format(now, html_table)

file_name = "searchnaver.html"  # 상대 경로 사용

with open(file_name, 'w', encoding='utf-8') as f:
    f.write(html_code)

print("생성한 파일:", file_name)
