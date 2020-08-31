## CRM приложение для работы с медоборудованием

Первоначальный деплой на heroku:

    "вспомнить, добавить"
    
## Добавить изменения в задеплоенное приложение:

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

Запуск тестов:

    python manage.py test bills