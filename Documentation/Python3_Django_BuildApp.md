# Python3 : Django - Building Web Apps

```sh
Set-ExecutionPolicy Unrestricted , and answer Y
python -V
conda install pip
pip freeze
mkdir D:\APP\djangostuff                                # Make Directory for Base location of he Application Files
python -m venv D:\APP\djangostuff\venv                  # Creating virtual environment for python
source D:\APP\djangostuff\venv\Scripts\activate         # Activating the virtual environemnt on linux
./venv/Scripts/activate                                 # Activating the virtual environemnt on windows - PowerShell
conda install pip                                       # Use Anaconda Package manager to first install pip
pip install django                                      # Use pip in future to install any modules in venv
python -m pip install --upgrade pip                     # If pip is on lower version upgarde using this command
pip freeze                                              # To validate what packages are installed in venv

(venv) (base) PS D:\app\djangostuff> pip freeze
asgiref==3.2.3
Django==3.0.2
pytz==2019.3
sqlparse==0.3.0

mkdir D:\APP\djangostuff\my_app
cd D:\APP\djangostuff\my_app
django-admin startproject todo_app .

(venv) (base) PS D:\app\djangostuff\my_app> ls
    Directory: D:\app\djangostuff\my_app
Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----         1/9/2020  12:43 PM                todo_app
-a----         1/9/2020  12:43 PM            649 manage.py


(venv) (base) PS D:\app\djangostuff\my_app> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK
(venv) (base) PS D:\app\djangostuff\my_app>


```

```sh
export APP_NAME="test"
mkdir -p /D/APP/$APP_NAME





```
