# Instructions

## Python commands

```
pip install pipenv ### installing pipenv
python3 -m venv /path/to/new/virtual/environment ### installing in specific location
source /path/to/new/virtual/environment ### activate specific virtual env for the project

## navigate to the project folder for which you want to create virtual environment
## this is where we can have multiple django projects with the same python version, django version ....

### CREATING PROJECT, APPLICATION AND RUNNING SERVER:

pipenv install django ## install django framework for this workdspace
pipenv shell ### launch the subshell in virtual environment (without using global, but project specific environment)
django-admin ### utility tool for django 
django-admin startproject projectname . ### create new project
python manage.py startapp application_name [port number] ### command for creating new app in project
python manage.py runserver [port number] ### command for starting app

## CREATING DB MODELS:

python manage.py makemigrations ### create models/ db tables command
python manage.py migrate ### execute migrations
python manage.py sqlmigrate todo 0001 ### this is to see what sql code will python generate for db in migration number 0001 of the app todo
python manage.py check ### this checks for any problems in your project without making migrations or touching the database.


### ADMINISTRATION

python manage.py createsuperuser # create admin/ super user

### TESTS
python manage.py test ### run all tests for project
python manage.py test [app_name] ### run test for only one app

### OTHER COMMANDS FOR SETTING UP 
pipenv --venv ### path to virtual environment. We need this to set up VS code to use virtual environment by default, not to set it up every time
# append \bin\python to this path
```


## Tools

1. django debug toolbar
2. 
