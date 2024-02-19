## INSTALLATIONS
```
pip install django==4.1.0
pip install djangorestframework
pip install django-allauth
pip install python-dotenv
pip install mysql-connector-python //THIS IS FOR mysql DB
pip install psycopg2-binary //THIS IS FOR postgresql DB
pip install africastalking
```
- OR
```
pip install -r requirements.txt
```
- To create a new requirements.txt file
```
 pip freeze > requirements.txt
```

## Adding a workflow
- Add a workflow with following commands
```
mkdir -p .github/workflows
touch .github/workflows/run-tests.yml
```

## Run server
```
source .venv/bin/activate
cd project
python3 manage.py runserver
```
- Deactivate virtual environment
```
source deactivate
or
deactivate
```

- Run migration
```
source .venv/bin/activate
cd project
python3 manage.py makemigrations
python3 manage.py migrate
```
