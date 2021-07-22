## Бот для отправки уведомлений о проверке работ.

Позволяет получать от бота в Telegram уведомления о проверке работ на сайте 
веб-разработчиков [Девман](https://dvmn.org).  

<a href="https://ibb.co/M1rtPzM"><img src="https://i.ibb.co/dpFVkNG/devman-bot-online.gif" alt="devman-bot-online" border="0"></a>

### Как установить

#### Скачать 

Python3 должен быть уже установлен.
[Скачать](https://github.com/Araime/devman-bot/archive/master.zip) этот репозиторий себе на компьютер.

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html)
для изоляции проекта.

#### Быстрая настройка venv

Начиная с Python версии 3.3 виртуальное окружение идёт в комплекте в виде модуля
venv. Чтобы его установить и активировать нужно выполнить следующие действия в
командной строке:  

Указать скачанный репозиторий в качестве каталога.
```sh
cd C:\Users\ваш_пользователь\Downloads\папка_репозитория
```
Установить виртуальное окружение в выбранном каталоге.
```sh
Python -m venv env
```
В репозитории появится папка виртуального окружения env  

<a href="https://imgbb.com/"><img src="https://i.ibb.co/Hn4C6PD/image.png" alt="image" border="0"></a>

Активировать виртуальное окружение.
```sh
env\scripts\activate
```
Если всё сделано правильно, вы увидите в командной строке (env) слева от пути 
каталога.  

<a href="https://imgbb.com/"><img src="https://i.ibb.co/MZ72r22/2.png" alt="2" border="0"></a>

#### Установить зависимости

Используйте `pip` (или `pip3`, есть конфликт с Python2) для установки 
зависимостей:

```sh
pip install -r requirements.txt
```

#### Переменные окружения

Создайте в корне репозитория файл `.env` и добавьте в него следующие строки:

```sh
DVMN_TOKEN=персональный_токен
TELEGRAM_TOKEN=токен_telegram_бота
TELEGRAM_CHAT_ID=ваш_персональный_chat_id
```

Персональный токен можно получить, на сайте [Девман](https://dvmn.org/api/docs/).  
Создать бота для Telegram и узнать его токен можно у [Отца Ботов](https://telegram.me/BotFather).  
Свой chat_id можно получить у [userinfobot](https://telegram.me/userinfobot).

### Запуск

Найти вашего бота в Telegram и написать ему сообщение `/start`

Запуск скрипта выполняется командой:

```sh
python main.py
```

### Деплой и запуск на Heroku

1. Зарегистрируйтесь на Heroku и создайте приложение (app):  
   
<a href="https://ibb.co/r5mDQ2Z"><img src="https://i.ibb.co/447hFRj/Screenshot-from-2019-04-10-17-43-30.png" alt="Screenshot-from-2019-04-10-17-43-30" border="0"></a><br />  

2. Опубликуйте код репозитория на свой GitHub.  
3. Привяжите свой аккаунт на GitHub к Heroku:  

<a href="https://ibb.co/Hqy7yvP"><img src="https://i.ibb.co/zZgsgc2/123.png" alt="123" border="0"></a>

4. Задеплойте проект на Heroku:  

<a href="https://ibb.co/kgpN9tF"><img src="https://i.ibb.co/1f3Fdkx/5353.jpg" alt="5353" border="0"></a>  

5. В разделе Resources включите Procfile:  

<a href="https://ibb.co/n3VbdLj"><img src="https://i.ibb.co/bHyPwKX/666.png" alt="666" border="0"></a>  

6. Перейти в раздел Settings и в пункте Config Vars указать DVMN_TOKEN, TELEGRAM_TOKEN,
   TELEGRAM_CHAT_ID:  

<a href="https://ibb.co/5x70h7H"><img src="https://i.ibb.co/FqPr4PT/8.png" alt="8" border="0"></a>  

7. Задеплоить повторно(пункт 4).  

Вы увидите сообщение о запуске в чате:  

<a href="https://ibb.co/JHXxvrg"><img src="https://i.ibb.co/Xtmy7FM/image.jpg" alt="image" border="0"></a>  

#### Работа с ботом из командной строки

Установить консольный [CLI client](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

Быстрый старт CLI:

Подключение к Heroku:
```sh
heroku login
```
Посмотреть список своих приложений:
```sh
heroku apps
```
Посмотреть логи:
```sh
heroku logs --app=имя_приложения
```
Статус бота:
```sh
heroku ps -a имя_приложения
```

[Руководство по Heroku CLI](https://devcenter.heroku.com/articles/using-the-cli)

### Цель проекта

Код написан в учебных целях, это часть курса по созданию [чат-ботов](https://dvmn.org/modules/chat-bots/)
на сайте веб-разработчиков [Девман](https://dvmn.org/api/docs/).