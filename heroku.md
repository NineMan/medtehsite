## Деплой на HEROKU

#### Первоначальный деплой:

Добавить в [requirements.txt](https://github.com/NineMan/medtehsite/blob/master/requirements.txt) ***Gunicorn***

    
Добавить в корень ***[Procfile](https://github.com/NineMan/medtehsite/blob/master/Procfile)***, он содержит настройку для использования единорога 


    web: gunicorn medtehsite.wsgi
    

Добавить в корень ***[runtime.txt](https://github.com/NineMan/medtehsite/blob/master/runtime.txt)***, он содержит версию python
    
    
    python-3.7.6
    

Установить [консоль heroku](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)

В консоли выполнить комнды

    heroku login
    git clone https://github.com/heroku/python-getting-started.git
    cd python-getting-started
    heroku create
    git push heroku master
    heroku open
    heroku logs --tail


#### Добавить изменения в задеплоенное приложение:

*считаем, что консоль heroku локально установлена*

    heroku login                                            // залогиниться в консоли
    git clone https://github.com/NineMan/medtehsite.git     // скопировать локально (например в папку publish)

    DEBUG = False                                           // отключаем debug mode в файле settins.py нашего проекта (metdehsite/medtehsite/settings.py)
    ALLOWED_HOSTS = ['http://mt-vlg.herokuapp.com/']        // обязательно нужно указать список доступных хостов (там же)

    cd mdtehsite
    heroku git:remote -a mt-vlg                             // подключаем репу к приложению на heroku (в консоли)
    git push heroku master                                  // пушим в мастер ветку на heroku

---

Эта команда подтянет изменения, произошедшие на репозитории GitHub:

    git pull    

После этого также можно отправлять на heroku сервер:
    
    git push heroku master

Терминал на heroku:

    heroku run bash -a <app>

Посмотреть логи:

    heroku logs --tail
