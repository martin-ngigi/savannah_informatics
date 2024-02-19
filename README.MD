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

## Create super admin
```
python3 manage.py createsuperuser
```

# Using all Auth:
- Link to authenticate users
```
[Link](http://127.0.0.1:8000/accounts/signup/)
```

## NB:
- Dont forget to add "Authorized JavaScript origins" in [Link](https://console.cloud.google.com/apis/credentials/) 
```
http://127.0.0.1:8000
```
- Also add "Authorized redirect URI"s in google console
```
http://127.0.0.1:8000
http://127.0.0.1:8000/accounts/google/login/callback/
```

# LOGIN WITH ALLAUTH:
- URL : http://127.0.0.1:8000/accounts/login/



-  users url:
- http://127.0.0.1:8000/users/all/
- http://127.0.0.1:8000/users/{user_id}/
- items url:
- http://127.0.0.1:8000/items/all/
- http://127.0.0.1:8000/items/all/{item_id}/
- orders url:
- http://127.0.0.1:8000/orders/all/
- http://127.0.0.1:8000/orders/all/{item_id}/
- http://127.0.0.1:8000/orders/user-orders/

## Testing all tests
```
python3 manage.py test
```

# Testing single module
```
python3 manage.py test profile_account.tests
python3 manage.py test items.tests
python3 manage.py test orders.tests
```


