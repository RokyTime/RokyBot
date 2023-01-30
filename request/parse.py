import requests
from bs4 import BeautifulSoup
import config

async def get_rate():
    link = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&client=ubuntu&hs=0l&channel=fs&biw=1415&bih=742&sxsrf=AJOqlzUPA3eBIax9vog5g2lwzigkJmfTkw%3A1674915305240&ei=6S3VY-umDuLLrgTA26zQBg&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgBMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgoIABBHENYEELADMgcIABCwAxBDMgcIABCwAxBDSgQIQRgASgQIRhgAUABYAGDwBmgBcAF4AIABAIgBAJIBAJgBAMgBCsABAQ&sclient=gws-wiz-serp'
    user_agent = config.my_user_agent
    page = requests.get(link, headers=user_agent).text
    soup = BeautifulSoup(page, 'html.parser')
    #<span class="DFlfde SwHCTb" data-precision="2" data-value="70.7275">70,73</span>
    res = soup.findAll("span", {"class" : "DFlfde SwHCTb", "data-precision" : "2"})

    link2 = 'https://coinmarketcap.com/ru/currencies/toncoin/'
    page2 = requests.get(link2, config.my_user_agent).text
    soup2 = BeautifulSoup(page2, 'html.parser')
    res2 = soup2.findAll("div", {"class" : "priceValue"})


    return f'1$ == {res[0].text}₽\n\
1TON == {res2[0].text.replace("₽", "")}₽'
    

async def get_anekdot():
    #<div class="text">- 67 процентов блондинок - полные дуры!<br>- А мне плевать. Я из остальных 13-ти!</div>
    link = 'https://www.anekdot.ru/random/anekdot/'
    user_agent = config.my_user_agent
    page = requests.get(link, headers=user_agent).text
    soup = BeautifulSoup(page, 'html.parser')
    res = soup.findAll("div", {"class" : "text"})
    return f'{res[0].text}'