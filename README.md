**CRM приложение для работы с медоборудованием.**
---
Первоначальный деплой на heroku:

    heroku login
    git clone https://github.com/NineMan/medtehsite.git
    cd mdtehsite
    heroku git:remote -a mt-vlg
    git push heroku master

Добавить изменения с репо:

    git pull
    git push heroku master
