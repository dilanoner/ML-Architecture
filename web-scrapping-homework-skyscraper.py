import bs4
import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter



response = requests.get('http://www.skyscrapercenter.com/buildings')

soup = bs4.BeautifulSoup(response.text, "html.parser")

prop = []  #prop adlı bir liste tanımladım

data = soup.findAll('td')   #tüm sütunları bulup data içine kaydettim
for row in data:  #data içindeki tüm satırlar sırasıyla data değişkenine eşitlendi
    data = row.get_text("", strip=True)
    prop.append(data) #her adımda data değişkeni prop listesine eklendi. (append komutu bu işe yarıyor)

del prop[:18]  #listenin ilk 18 elemanını sildim. Siteye bakarsan renk kodlarının olduğu bir satır daha var. O satırı istemiyorum. O yüzden onları sildim.
#print(prop)

a = open('sky', 'w' )  #her çalıştırdığımda dosyanın üstüne yazıyor. Bu yüzden önce dosyayı açıp temizliyorum.
a.truncate() #temizledim
a.close() #kapattım



f = open('sky','a') # open new file, make sure path to your data file is correct

p = 0 # initial place in array

l = len(prop)-1 # length of array minus one


f.write("Number, Status, Building Name, City, Height(m), Height (feet), Floors, Completion, Material, Use\n") #write headers


while p < l: # while place is less than length
    f.write(prop[p] + ", ") # w
    p = p + 1 # increment
    f.write(prop[p] + ", ") #liste elemanı koy sonra virgül koy
    p = p + 1 # increment
    f.write(prop[p] + ", ")
    p = p + 1 # increment
    f.write(prop[p] + ", ")
    p = p + 1 # increment
    f.write(prop[p] + ", ")
    p = p + 1 # increment
    f.write(prop[p] + ", ")
    p = p + 1 # increment
    f.write(prop[p] + ", ")
    p = p + 1 # increment
    f.write(prop[p] + ", ")
    p = p + 1 # increment
    f.write(prop[p] + ", ")
    p = p + 1 # increment
    f.write(prop[p] + ", ")
    p = p + 1 # increment
    f.write(prop[p] + "\n") #liste elemanı koy sonra virgül koy. İlk satır bitti bir de alt satıra geç
    p = p + 1 # increment


f.close() # close file

county = pd.read_csv('sky.csv')

#print(county.to_string()) #bütün sütunlar görünsün diye to_string

city = []

t=4

while t < 1100:
    city.append(prop[t])
    t=t+11

how_many = dict(Counter(city))

fig= plt.figure()

fig.suptitle('Building per City')
plt.xlabel('City')
plt.ylabel('Number')

plt.bar(range(len(how_many)), list(how_many.values()), align='center')
plt.xticks(range(len(how_many)), list(how_many.keys()), rotation=90)


plt.show()