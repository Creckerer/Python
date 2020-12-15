import requests
import re
import sys
from bs4 import BeautifulSoup
myheader = {}
myheader['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.1.2222.33 Safari/537.36'
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

#print(file1)
#print(soup)
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
#href_to_torrents = soup.findall('div', class="download")['onclick']
i=0
for all_name in soup.find_all('div', {'class': "file-item"}):
     for name in all_name:
        print("Film name  :  " + str(name))

for all_href in soup.find_all('span', {'class': "download"}):
    print("333 :  " + str(all_href))
    for href1 in all_href.find_all('span', )):
        print("eeee :   " + href1)



file1.close()

eo src="https://ix1.cdnlast.com/s/585c77dbdfffa1d5d987bff624c879f299f/uhd_mc/Mulan.2020.BDRip.2160p.4K.UHD.rus_480.mp4?vs4-origin" x-webkit-airplay="allow" preload="none" style="width: 100%; height: 100%; object-fit: contain; transition: filter 0.2s linear 0s; min-height: auto; max-height: none; min-width: auto; max-width: none; position: static; left: 0px; top: 0px;"></video>