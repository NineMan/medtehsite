##  Описание проекта 

CRM приложение для работы с медоборудованием


  - Приложения проекта:
  
    - bills - модуль для отслеживания запчастей заказанных по безналу
    - cash - контроль закупок за наличку - в разработке
    - order - отслеживание заявок на обслуживание - в разработке
    - repair - модуль для приёма, выдачи и отслеживания ремонта - в разработке

#### Использовано в проекте:

```bash
  * front - Bootstrap 4.5
  * back  - Django 3.1
```

#### Запуск приложения

1 Установить виртуальное окружение и запустить его

2 Скопировать себе в репозитарий 

```python
git clone https://github.com/NineMan/medtehsite.git
```

3 Установить зависимости
  
```python
pip install -r requirements.txt
```
    
4 Создать таблицы в базе данных 
  
```python
python manage.py migrate
```
    
5 Создать админа
  
```python
python manage.py createsuperuser
```
    
6 Заполнить базу тестовыми данными
  
```python
python manage.py loaddata medtehsite/apps/bills/fixtures/test_data.json
``` 

7 Запустить приложение
  
```python
python manage.py runserver
```

Запуск тестов:

```python
python manage.py test bills
```

