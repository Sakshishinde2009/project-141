
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

NEW_URL = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(NEW_URL)

soup = BeautifulSoup(page.text,"html.parser")

star_table = soup.find_all("table")

table_rows = star_table[7].find_all("tr")

temp_list = []

for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

star_name = []
radius = []
distance = []
mass = []

for i in range(1,len(temp_list)):
    star_name.append(temp_list[i][0])
    distance.append(temp[i][5])
    radius.append(temp[i][8])
    mass.append(temp[i][7])

#convert to csv
headers = ["Star_name","Distance","Mass","Radius"]
df2 = pd.DataFrame(list(zip(star_name,distance,mass,radius)),columns=headers)
print(df2)

df2.to_csv("Brown_stars.csv",index= True,index_label= "id")
