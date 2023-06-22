# post_page

## 1. Create virtual environment with python 3.10 and install packages

`pip install -r requirements.txt`

## 2. Install postgresql, create db postapp in Postgresql

`CREATE DATABASE postapp PASSWORD 'password'`

## 3. Make migrations and migrate

`python manage.py makemigrations`

`python manage.py migrate`

## 3. Run server, the server is host on port 8000

`python manage.py runserver`
