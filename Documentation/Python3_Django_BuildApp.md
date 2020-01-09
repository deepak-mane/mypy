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



```

```sh
export APP_NAME="test"
mkdir -p /D/APP/$APP_NAME





```
