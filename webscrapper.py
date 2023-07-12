from bs4 import BeautifulSoup as bs
import requests
import time
import csv
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
headers = {"Name","Radius","Mass","Distance"}

web_data = requests.get(START_URL)
print(web_data)

soup = bs(web_data.text,"html.parser")
table = soup.find("table")
print(table.head)

temp_list = []
table_row = table.find_all("tr")

for tr in table_row:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

name = []
radius = []
mass = []
distance = []

for row in temp_list:
    name.append(temp_list[row][1])
    radius.append(temp_list[row][6])
    mass.append(temp_list[row][5])
    distance.append(temp_list[row][3])

df = pd.DataFrame(list(zip(name,radius,mass,distance)),columns=["Stars","Radius","Mass","Distance"])
df.to_csv("Stars")

