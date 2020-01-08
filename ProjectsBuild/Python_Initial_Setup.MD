# Python Initial Setup


```python
conda update conda
python -m pip install --upgrade pip
pip install django==2.2.5
pip install django-dependency
python manage.py migrate

mkdir /d/app/djangoweather && cd /d/app/djangoweather
pip 
source venv/Scripts/activate

python manage.py runserver 7000

Non non-windows
python manage.py createsuperuser

For windows git-bash
winpty python manage.py createsuperuser

To Create New App
python manage.py startapp lookup                                                                                   (venv)

```

- __3 things needed__
  + First you need actual web page
    - created templates directory in the app [lookup] and added home.html file init.
  + template
    - created views.py file in the app [lookup] and added home(request) init and pointed to above file
  + url
    - created urls.py file in the app [lookup] and added path('', views.home, name="home"),
    
