from bs4 import BeautifulSoup
import requests
import webbrowser
import pprint

urlstring = []
new_list = []
lol = input("Enter in search terms: ")
url = "https://www.google.com/search?q=" + lol
searchdict = {}
compdict = {}
response = requests.get(url)
k = 1
with open('output.html', 'wb') as f:
    f.write(response.content)
webbrowser.open('output.html')


soup = BeautifulSoup(response.text, 'lxml')
for tag in soup.find_all(class_="BNeawe vvjwJb AP7Wnd"):
    searchdict[k] = tag.text
    k += 1
k = 1
for a in soup.find_all('a'):
    urlstring.append(a.get_attribute_list('href')[0])
for x in urlstring:
    if "/url?q=" in x:
        compdict[k] = x
        k += 1

print(new_list)

pprint.pprint(searchdict)
pprint.pprint(compdict)




cite = int(input("Enter in the number of the link you want: "))

print(searchdict[cite])
now = (compdict[cite])
newrec = "https://www.google.com/search?q=" + now





