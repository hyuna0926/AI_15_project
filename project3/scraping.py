import requests
from bs4 import BeautifulSoup
import re

def get_page(page_url):
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup, page


#제목들고오기
def title(page_num):
    url = f"http://www.yes24.com/24/Category/Display/001001046011001?FetchSize=40&ParamSortTp=05&PageNumber={page_num}"
    
    soup, page = get_page(url)
    list=[]
    for i in range(0,80):
        list.append({'title':soup.select('div.goods_name>a')[i].text})
        title1 = list[0::2]
    return title1

#페이지별
def get_title(page_num):
    url = f"http://www.yes24.com/24/Category/Display/001001046011001?FetchSize=40&ParamSortTp=05&PageNumber={page_num}"
    
    soup, page = get_page(url)

    title_1 =[]
    for page_n in range(page_num):
        title_1 +=title(page_n)
    return title_1

"""
----------------------------------

"""

#가격
def price(page_num):
    url = f"http://www.yes24.com/24/Category/Display/001001046011001?FetchSize=40&ParamSortTp=05&PageNumber={page_num}"
    
    soup, page = get_page(url)

    price = soup.select('div.goods_price>em.yes_b')
    price_1=[]

    for r in range(len(price)):
        b = float(re.sub(",","",price[r].text))
        price_1.append({'price':b})
    return price_1

def get_price(page_num):
    url = f"http://www.yes24.com/24/Category/Display/001001046011001?FetchSize=40&ParamSortTp=05&PageNumber={page_num}"
    
    soup, page = get_page(url)

    star_1 =[]
    for page_n in range(page_num):
        star_1 +=price(page_n)
    return star_1


#별점
def star(page_num):
    url = f"http://www.yes24.com/24/Category/Display/001001046011001?FetchSize=40&ParamSortTp=05&PageNumber={page_num}"
    
    soup, page = get_page(url)
    star1=[]

    star =soup.select('span.gd_rating > em.yes_b')

    for r in range(len(star)):
        c = float(star[r].text)
        star1.append({'star':c})
    return star1

#페이지별
def get_star(page_num):
    url = f"http://www.yes24.com/24/Category/Display/001001046011001?FetchSize=40&ParamSortTp=05&PageNumber={page_num}"
    
    soup, page = get_page(url)

    star_1 =[]
    for page_n in range(page_num):
        star_1 +=star(page_n)
    return star_1