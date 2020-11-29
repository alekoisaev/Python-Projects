import requests
from bs4 import BeautifulSoup

r = requests.get("https://goal.ge/")
c = r.content

soup = BeautifulSoup(c, "html.parser")

all1 = soup.find_all("div", {"class": "news-lenta-item"})

sataurebi = []
dro = []

dict1 = {}

for item in all1:
    dro.append(item.find_all("date")[0].text)
    sataurebi.append(item.find_all("div", {"class": "news-lenta-item-title"})[0].text)

for i, x in zip(sataurebi, dro):
    dict1[x] = i

counter = 0
for k, v in dict1.items():
    counter += 1
    print(str(counter) + ". - ", k, "-", v)
