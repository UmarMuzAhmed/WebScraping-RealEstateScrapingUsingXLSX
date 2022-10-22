import shelve
import requests
from bs4 import BeautifulSoup
import openpyxl

excel= openpyxl.Workbook()
sheet=excel.active
sheet.title="HOUSING'S"
sheet.append(['title','address','price','area'])

url='https://www.pararius.com/apartments/amsterdam'
page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')
lists=soup.find_all('section',class_='listing-search-item')


for list in lists:
    title=list.find('a',class_='listing-search-item__link listing-search-item__link--title').get_text(strip=True)
    address=list.find('div',class_='listing-search-item__sub-title').get_text(strip=True)
    price=list.find('div',class_='listing-search-item__price').get_text(strip=(True))
    area=list.find('li',class_='illustrated-features__item illustrated-features__item--surface-area').get_text(strip=(True))
    sheet.append([title,address,price,area])

excel.save("HOUSING IN AMSTERDAM.xlsx")
        
