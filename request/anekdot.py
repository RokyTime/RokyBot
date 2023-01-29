import config
import requests
from bs4 import BeautifulSoup


async def get_anekdot():
    #<div class="text">- 67 процентов блондинок - полные дуры!<br>- А мне плевать. Я из остальных 13-ти!</div>
    link = 'https://www.anekdot.ru/random/anekdot/'
    user_agent = config.my_user_agent
    page = requests.get(link, headers=user_agent).text
    soup = BeautifulSoup(page, 'html.parser')
    res = soup.findAll("div", {"class" : "text"})
    return f'{res[0].text}'