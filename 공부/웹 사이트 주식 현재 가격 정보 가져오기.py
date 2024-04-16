import requests
from bs4 import BeautifulSoup

base_url = "https://finance.naver.com/item/main.nhn"
stock_code = "005930"

url = base_url + "?code=" + stock_code

html = requests.get(url).text
soup = BeautifulSoup(html,'lxml')

print(url)

#%%
soup.select_one('p.no_today')

#%%

stock_price = soup.select_one('p.no_today span.blind').get_text()
stock_price

#%%
import requests
from bs4 import BeautifulSoup

def get_current_stock_price(stock_code):
    
    base_url = "https://finance.naver.com/item/main.nhn"
    url = base_url + "?code=" + stock_code


    html = requests.get(url).text
    soup = BeautifulSoup(html,'lxml')
    
    stock_price = soup.select_one('p.no_today span.blind').get_text()
    
    return stock_price

#%%
stock_code = "005930"
current_stock_price = get_current_stock_price(stock_code)
current_stock_price

#%%

company_stock_codes = {"삼성전자":"005930", "현대차":"005380","두산로보틱스":"454910"}

print("[현재 주식 가격(원)]")
for company,stock_code in company_stock_codes.items():
    current_stock_price = get_current_stock_price(stock_code)
    print(f"{company} : {current_stock_price}")