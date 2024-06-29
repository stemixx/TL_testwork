# TL_testwork
Задача.

Создайте веб страницу, которая будет выводить древовидную структуру отделов со списком сотрудников
Информация о каждом сотруднике должна храниться в базе данных и содержать следующие данные
1.  ФИО
2.  Должность
3.  Дата приема на работу
4.  Размер заработной платы
5.  Подразделение – подразделения имеют структуру до 5 уровней

Дерево должно отображаться в свернутом виде.
База данных должна содержать не менее 50000 сотрудников и 25 подразделений в 5 уровнях иерархий.
Управление записями CRUD  через административную часть Django.
Django 3+, Python 3.5+, база на свое усмотрение.
Используйте Twitter Bootstrap для создания базовых стилей вашей страницы.

***********
step-by-step project performance
```
mkdir TL_testwork | cd TL_testwork
```
Make a python virtual environment  and start Django project
```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
django-admin startproject tl_testwork
cd tl_testwork | python manage.py startapp employee
```
Create database tl_testwork and database user tl_user in pgAdmin 4.
After adding models and 'employee' in INSTALLED_APPS:
```
python manage.py makemigrations
python manage.py migrate
```
Generate random data to database:
```
python manage.py generate_data_to_db
```   
Create django admin user:
```
python manage.py createsuperuser
```
After adding views, templates and other necessary code start development server:
```
python manage.py runserver 127.0.0.1:8001
```
***********
Cloning this project
```
mkdir TL_testwork | cd TL_testwork
git clone https://github.com/stemixx/TL_testwork
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
Create database tl_testwork and database user tl_user in pgAdmin 4 according to DATABASES in settings.py.
Generate random data to database:
```
python manage.py generate_data_to_db
```   
Start server
```
python manage.py runserver 127.0.0.1:8001
```