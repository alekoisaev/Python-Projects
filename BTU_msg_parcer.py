import requests
from bs4 import BeautifulSoup

s = requests.Session()
r = s.get("https://classroom.btu.edu.ge/ge/login")

print("===================================")
print("--- |Welcome to BTU classroom |---")
print("===================================")
login = input("Enter username: ")
pas = input("Enter password: ")
student_name = input("Enter Student name (ქართულად): ")

data = {'username': login,
        'password': pas
        }

r = s.post("https://classroom.btu.edu.ge/ge/login/trylogin", data=data)

index = 21212
url = 'https://classroom.btu.edu.ge/ge/messages/compose/{}'.format(index)
r = s.get(url).content

soup = BeautifulSoup(r, "html.parser")

all1 = soup.find_all("div", {"class": "col-sm-14"})

sia = []
for item in all1:
    sia.append(item.text)

while index > 1:
    index += 1
    url = 'https://classroom.btu.edu.ge/ge/messages/compose/{}'.format(index)
    r = s.get(url).content
    soup = BeautifulSoup(r, "html.parser")
    all1 = soup.find_all("div", {"class": "col-sm-14"})

    sia.clear()

    for item in all1:
        sia.append(item.text)
    name = sia[0].strip()
    print("Loading ...  | ", name, "|")
    if student_name == name or student_name in name:
        print("--------------------------")
        print("I Find him/her BITCH! -", name)
        print(url)
        break
