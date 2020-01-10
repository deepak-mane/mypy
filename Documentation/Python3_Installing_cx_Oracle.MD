# Python3 : Installing cx_Oracle on windows

- [Reference link1](https://www.foxinfotech.in/2018/09/how-to-install-cx_oracle-for-python-on-windows.html)
- [cx-oracle.readthedocs.io](https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html)

Steps to Download and Install cx_Oracle Package for Python on Windows
1. Click on the Download cx_Oracle link to download the package from Github.
1. Extract the zip file to a folder on Windows. For example, F:\cx_oracle.
1. Now open the command prompt and change the current directory to the F:\cx_oracle directory to install cx_Oracle package.
1. Then run the following command.
```python python -m pip install cx_Oracle --upgrade pip ```
It will install the cx_Oracle package for Python on Windows, and you will get the messages as shown below.

```cmd
(venv) [C:\cx_Oracle]
>python -m pip install cx_Oracle --upgrade
Collecting cx_Oracle
  Downloading https://files.pythonhosted.org/packages/49/5a/c445cf6702b7ce9c46ea85406195bc29ece54ed82dc5534f115db47d5069/cx_Oracle-7.3.0-cp37-cp37m-win_amd64.whl (189kB)
    100% |████████████████████████████████| 194kB 1.9MB/s
Installing collected packages: cx-Oracle
Successfully installed cx-Oracle-7.3.0
You are using pip version 19.0.3, however version 19.3.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

(venv) [C:\cx_Oracle]
>python -m pip install --upgrade pip
Collecting pip
  Downloading https://files.pythonhosted.org/packages/00/b6/9cfa56b4081ad13874b0c6f96af8ce16cfbc1cb06bedf8e9164ce5551ec1/pip-19.3.1-py2.py3-none-any.whl (1.4MB)
    100% |████████████████████████████████| 1.4MB 3.3MB/s
Installing collected packages: pip
  Found existing installation: pip 19.0.3
    Uninstalling pip-19.0.3:
      Successfully uninstalled pip-19.0.3
Successfully installed pip-19.3.1
```


Now Test The Connection To Oracle From Python
Open Python IDE and give the following commands one by one to test the connection. Change your_username and your_psw to your database username and password.

```python
 
import cx_Oracle
connection = cx_Oracle.connect("your_username", "your_psw", "localhost/orcl")
cursor = connection.cursor()
cursor.execute("""select to_char(sysdate, 'dd-mon-yyyy') from dual""")
for cdate in cursor:
print("Today the date is ", cdate)

Output
Today the date is ('05-sep-2018',)

```


