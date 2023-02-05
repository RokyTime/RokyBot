import requests
import config
from create_bot import bot



async def get_weather():
    city_id = config.city_id
    appid = config.appid
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid}, timeout=5)
        data = res.json()
        text = f'🌧️Погода:{data["weather"][0]["description"]},\n\n\
🌡️Температура:{data["main"]["temp"]} C°,\n\n\
🥶Ощущается как:{data["main"]["feels_like"]} C°,\n\n\
🌡️Минимальная температура:{data["main"]["temp_min"]} C°,\n\n\
🌡️Максимальная температура:{data["main"]["temp_max"]} C°.'
        return text
    except Exception as e:
        for admin in config.admin_ID:
            bot.send_message(admin , f'Exception (weather):{e}')