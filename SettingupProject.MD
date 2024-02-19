# Setting up the environment on Mac
- Create a directory  and navigate to directory
```
 mkdir savannahinformatics
 cd savannahinformatics
```
- create a virtual environment and activate it
```
python3 -m venv .venv
source .venv/bin/activate
```
- Install pip and django==4.1.0
```
pip install django==4.1.0
```
- Start project and navigate to directory
```
django-admin startproject project
```
- Run server
```
source .venv/bin/activate
cd project
python3 manage.py runserver
```
