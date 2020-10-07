import requests

from bs4 import BeautifulSoup

url = "https://www.n11.com/mobilya/karyola-yatak-baza/yatak"

html = requests.get(url).content

soup = BeautifulSoup(html, "html.parser")

list = soup.find_all("li", {"class": "column"}, limit=10)
for li in list:
    name = li.div.a.h3


    print(name)


