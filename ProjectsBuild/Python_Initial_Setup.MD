# Python Initial Setup


```python
conda update conda
python -m pip install --upgrade pip

mkdir /d/app/djangoweather && cd /d/app/djangoweather
python -m venv myvenv # [/path/to/new/virtual/environment]
source venv/Scripts/activate

pip install django==2.2.5
pip install django-dependency
pip freeze # [ Check what got installed]

Creating a project
==================================
django-admin startproject mysite


To Create App - weather (first app -main)
==================================
python manage.py startapp weather

python manage.py migrate  # [ move the models into database  related to admin ]
To Start the Webserver
==================================
python manage.py runserver 7000 # [ start the light weiht webserver of your app ]

Non non-windows
python manage.py createsuperuser

For windows git-bash
winpty python manage.py createsuperuser

To Create Additional New App
==================================
python manage.py startapp lookup

```

1. __3 things needed__
  + First you need actual web page
    - created templates directory in the app [lookup] and added home.html file init.
  + template
    - created views.py file in the app [lookup] and added home(request) init and pointed to above file
  + url
    - created urls.py file in the app [lookup] and added path('', views.home, name="home"),
    
2. __Creating Navbar__
