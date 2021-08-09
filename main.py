from bs4 import BeautifulSoup
import requests
import webbrowser
import pprint

url = input("Enter url: ")
req = requests.get(url)
webbrowser.open(url)
soup = BeautifulSoup(req.text, 'lxml')
dls = soup.find_all("dl",{'class':'si_row'})
for dl in dls:
    atag = dl.find('a')
    if atag:
        author_link = atag.get('href')
        author_name = atag.get_text()
        print(author_link)
        print(author_name)

span_date = soup.find('span',{'class':'item_date'})
if span_date:
    date = span_date.get_text()
    print(date)





