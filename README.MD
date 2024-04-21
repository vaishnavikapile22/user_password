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

![Screenshot (76)](https://github.com/vaishnavikapile22/user_password/assets/149785862/434a5795-0394-4657-b8fa-5540b76f8f80)

#127.0.0.1:8000/dashboard

![Screenshot (77)](https://github.com/vaishnavikapile22/user_password/assets/149785862/2af32755-1f3d-44f7-ad89-695207e294d5)


# 127.0.0.1:8000/login

![Screenshot (78)](https://github.com/vaishnavikapile22/user_password/assets/149785862/82002723-a59e-4175-9a00-7a8577889dd2)


#127.0.0.1:8000/admin

![Screenshot (79)](https://github.com/vaishnavikapile22/user_password/assets/149785862/e18fb58c-e570-4bdd-853d-42f67b46e35b)


#127.0.0.1:8000/admin

![Screenshot (80)](https://github.com/vaishnavikapile22/user_password/assets/149785862/518f0df3-26bc-4ebd-ae1e-53483482f4a6)

#all user data ho login or register

![Screenshot (81)](https://github.com/vaishnavikapile22/user_password/assets/149785862/795f20f8-8d04-4e80-abd0-8976d7b8bcca)

#  127.0.0.1:8000/history


![Screenshot (82)](https://github.com/vaishnavikapile22/user_password/assets/149785862/15e75e38-c3c7-471b-8c05-de9e0ad07ba9)


