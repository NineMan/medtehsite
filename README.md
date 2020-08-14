CRM приложение для работы с медоборудованием.


Деплой на heroku:
Первоначально:

heroku login
git clone https://github.com/NineMan/medtehsite.git
cd mdtehsite
heroku git:remote -a mt-vlg
git push heroku master

Добавить изменения с репоЖ
git pull
git push heroku master
