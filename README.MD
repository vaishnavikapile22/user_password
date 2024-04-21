#start project 

django-admin startproject myproject

# start app 

python manage.py startapp backend

#CREATE VARTIUAL ENVIORMENT

python -m venv env

. env/scripts/activate

#tree

myproject
├───backend
│   ├───migrations
│   │   └───__pycache__
│   ├───static
│   │   ├───admin
│   │   │   ├───css
│   │   │   │   └───vendor
│   │   │   │       └───select2
│   │   │   ├───img
│   │   │   │   └───gis
│   │   │   └───js
│   │   │       ├───admin
│   │   │       └───vendor
│   │   │           ├───jquery
│   │   │           ├───select2
│   │   │           │   └───i18n
│   │   │           └───xregexp
│   │   ├───css
│   │   └───js
│   ├───templates
│   └───__pycache__
└───myproject

# in seettings.py

INSTALLED_APPS = [

         'backend',
]


STATIC_ROOT = r'C:\Users\Admin\Downloads\assigment\myproject\backend\static'

STATIC_URL = 'static/'

STATICFILES_DIRS = [
   
    os.path.join(BASE_DIR, 'static'),

]

#after create static file 

pip install collastatic

pip install flet

python manage.py makemigrations

python manage.py make migrate


python manage.py createsuper user

python manage.py runserver

#OUTPUT

# 127.0.0.1:8000/register

![Screenshot (76)](https://github.com/vaishnavikapile22/1/assets/149785862/c1866b49-ecdf-40fd-9d49-5921cc66275b)

#127.0.0.1:8000/dashboard

![Screenshot (77)](https://github.com/vaishnavikapile22/1/assets/149785862/41d3c813-acd6-4808-a332-ea7774c0486d)


#127.0.0.1:8000/login

![Screenshot (78)](https://github.com/vaishnavikapile22/1/assets/149785862/a9d6826c-981a-4265-a3a5-0e0ef7fa5ed4)


#127.0.0.1:8000/admin

![Screenshot (79)](https://github.com/vaishnavikapile22/1/assets/149785862/fda003bd-a8b4-4e56-8ccd-84ee02f36ded)


#127.0.0.1:8000/admin

![Screenshot (80)](https://github.com/vaishnavikapile22/1/assets/149785862/55f26f59-d01e-403a-975f-d311844609d7)


#all user data who login or register

![Screenshot (81)](https://github.com/vaishnavikapile22/1/assets/149785862/127fb3e8-511c-43e0-9bdc-b6a81d4b8e91)


#127.0.0.1:8000/history

![Screenshot (82)](https://github.com/vaishnavikapile22/1/assets/149785862/35ccffdc-9a3a-43f8-b743-040bcd1fd0cf)



