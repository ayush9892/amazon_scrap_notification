from bs4 import BeautifulSoup as soup
import requests
import lxml

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
            'Accept-language':'en'
    }
url = 'https://www.amazon.in/Acer-i5-11400H-15-6-inch-Graphics-Keyboard/dp/B09B2F2DMK/ref=sr_1_1_sspa?dchild=1&keywords=acer+nitro+5&qid=1634024246&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzNDBYR0NSSVJMR1lFJmVuY3J5cHRlZElkPUEwNTA1NjQ1U0NGTjUxNTM5Q0g4JmVuY3J5cHRlZEFkSWQ9QTA5NTU2OThLTE9ONTdWQjIxVTAmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'

html = requests.get(url,headers=header)
sobj = soup(html.text, 'lxml')

# print(sobj.prettify())

name = soup.select_one(selector="productTitle")
print(name)