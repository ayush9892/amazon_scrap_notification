from bs4 import BeautifulSoup as soup
import requests
import lxml  # lxml provides a very simple and powerful API for parsing XML and HTML. It supports one-step analysis.

def get_link_data(url):

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
            'Accept-language':'en'
    }
    
    html = requests.get(url,headers=header)
    sobj = soup(html.text, "lxml")

    name = sobj.select_one(selector="#productTitle").getText()
    name = name.strip()

    price = sobj.select_one(selector=".a-offscreen").getText()


    price = price[1:]
    price = price.replace(',' , '')  
    price = float(price)    

    return name, price




