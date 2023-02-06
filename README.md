# Telegram-бот-напоминалка для личного пользования.
Бот исключительно для взаимодействия в личных сообщениях. Имеет функции обращения к `API` `openwethermap`, парса биржи криптовалюты, поискового запроса гугл, парса сайта с анекдотами, хранения и редактирования расписания пользователя в базе данных. Бот имеет пассивную функцию в 5 утра отправлять содержание команды `Инфа(смотреть ниже)` + расписание и анекдот дня.
## Команды бота:
+ Инфа - Бот отправляет курс TON, доллара и погоду на данный момент.
+ Анекдот - Команда для парса сайта с рандомной выдачей анекдотов.
+ Расписание - Читает из базы данных и отправляет расписание юзера.
+ Добавить расписание - Меню редактирования расписания в базе данных через Inline-клавиатуру.
# Запуск бота.
Перед запуском нужно внести некоторую конфигурацию
требуется в корневой папке проекта создать файл с именем `config.py` с таким вот содержимым:
```Python
TOKEN=''
admin_ID=[]
city_id= 
appid=""
my_user_agent={'User-agent' : ''}
```
В поле `TOKEN` нужно вписать токен, полученный при создании бота. В поле `admin_ID` через запятую перечислить ID пользователей бота, даже если храниться одно значение, хранить в списке. Поля `city_id` и `appid` параметры для взаимодействия с `API` `openwethermap`. В поле `my_user_agent` под ключем `'User-agent'` следует записать юзер-агент, от лица которого будут производиться запросы для парса. Получить его можно, вписав в поиск гугл `my user agent`.
 
___


Для запуска бота с `Linux Ubuntu` требуется в каталоге проекта открыть терминал, после чего командой `source venv\bin\activate` запустить виртуальное окружение. После этой операции в корневой папке проекта нужно запустить файл `bot_telegram.py` командой `python3 bot_telegram.py`
___

Для запуска бота с `Windows` требуется в корневом каталоге проекта создать виртуальное окружение `Python` командой `python -m venv venv`. После чего, открыв терминал в корневой папке проекта прописать `venv\scripts\activate`, после запустить `Python`-файл `python bot_telegram.py `