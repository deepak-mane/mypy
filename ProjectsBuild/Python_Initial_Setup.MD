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
```
