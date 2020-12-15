import requests
import re
from bs4 import BeautifulSoup
myheader = {}
myheader[
    'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.1.2222.33 Safari/537.36'
url = 'https://filmix.co/drama/135512-mulan-film-2020.html'
try:
    response = requests.get(url, headers=myheader)
    soup = BeautifulSoup(response.text, features="html.parser")
except requests.exceptions.RequestException:
    print('Check your url')
with open('results', 'w') as file:
    file.write(response.text)
file.close()
file1 = open('results', 'r')
href_to_find = r"\w+://\w+.\w+/download/\d+"
href_returned = re.findall(href_to_find, file1.read())
href_returned = href_returned[0]
href_to_torrents = soup.find('a', href=href_returned)['href']
print(href_to_torrents)
try:
    response = requests.get(href_to_torrents, headers=myheader)
    soup = BeautifulSoup(response.text, features="html.parser")
except requests.exceptions.RequestException:
    print('Check your second url')
with open('results', 'w') as file:
    file.write(response.text)
file.close()
file1 = open('results', 'r')

href_to_find = r"\w+.\w+.\w+=\'\w+://\w+.\w+/download-file/\d+\'"
href_returned = re.findall(href_to_find, file1.read())
href_returned = href_returned[0]
print(href_returned)
i=0
for all_name in soup.find_all('div', {'class': "file-item"}):
    for name in all_name:
        all_href = soup('span', {'class': "download"})[i]['onclick']
        all_href = all_href.split("=")
        all_href = all_href[1]
        i+=1
        print("Film name  :  " + str(name) + ", Link to film  :  " + str(all_href))
        with open('last', 'a') as lol:
            lol.write("Film name  :  " + str(name) + ", Link to film  :  " + str(all_href) + "\n")
lol.close()
file1.close()
