import pandas as pd
import requests
from bs4 import BeautifulSoup
Product_name=[]
Prices=[]
Ratings=[]

for i in range(2,8):
    url="https://www.flipkart.com/search?q=mobiles+under+50000&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_5_0_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_5_0_na_na_na&as-pos=5&as-type=HISTORY&suggestionId=mobiles+under+50000&requestId=d3d8ff23-85f0-48af-a964-da3348285776&page="+str(i)

    r=requests.get(url)
    #print(r)

    soup= BeautifulSoup(r.text, "lxml")
    box=soup.find("div", class_="DOjaWF gdgoEp")

    names= box.find_all("div", class_="KzDlHZ")

    for i in names:
        name= i.text
        Product_name.append(name)
    #print(Product_name)

    prices= box.find_all("div", class_="Nx9bqj _4b5DiR")
    for i in prices:
        prices=i.text
        Prices.append(prices)
    #print(Prices)   

    ratings=box.find_all("div", class_="XQDdHH")
    for i in ratings:
        ratings=i.text
        Ratings.append(ratings)
    #print(Ratings)

    if len(Product_name) > len(Prices):
        Prices.extend([None] * (len(Product_name) - len(Prices)))
    elif len(Prices) > len(Product_name):
        Product_name.extend(["Unknown"] * (len(Prices) - len(Product_name)))

    if len(Product_name) > len(Ratings):
        Ratings.extend([None] * (len(Product_name) - len(Ratings)))
    elif len(Ratings) > len(Product_name):
        Product_name.extend(["Unknown"] * (len(Ratings) - len(Product_name)))



df=pd.DataFrame({"Product Name":Product_name,"Prices":Prices,"Ratings":Ratings})
print(df)

df.to_csv("D:/WebScrapingFlipkart_mobiles_under_50k.csv")
