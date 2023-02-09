# Egyptian national ID validator
Egyptian national ID validator and data-extractor API V1.

<br/>

# Valid Egyptian national ID

* A valid Egyptian national ID must follow this rules:
 1. Must be 14 digits 
 2. Negative numbers not allowed
 3. Have to start with 2 or 3
 4. [From 2nd to 7th digits] (DD MM YY) it must be a valid birth date (can't be in the future)
 5. [8th and 9th digits] represent the government code (it can't be unknown government code) the standard codes are : 
    * ```python
        {
            1: 'Cairo',
            2: 'Alexandria',
            3: 'Port Said',
            4: 'Suez',
            11: 'Damietta',
            12: 'Daqahliya',
            13: 'Sharqiya',
            14: 'Qalioubiya',
            15: 'Kafr El Sheikh',
            16: 'Gharbiya',
            17: 'Monofiya',
            18: 'Beheira',
            19: 'Ismailia',
            21: 'Giza',
            22: 'Bani Suef',
            23: 'Fayyoum',
            24: 'Minya',
            25: 'Assiut',
            26: 'Sohag',
            27: 'Qena',
            28: 'Aswan',
            29: 'Luxor',
            31: 'Red Sea',
            32: 'New Valley',
            33: 'Matrouh',
            34: 'North Sinai',
            35: 'South Sinai',
            88: 'Born Abroad',

        }
        ```
 


# Basic functionality
1. Login and Registration.
2. ID validation. 
3. Data Extraction.


<br/>

# Getting started

## Installation

make a new folder for the project and open this folder in the Terminal/Windows (PowerShell) and run this command

``` bash
git clone https://github.com/omar-bendary/Shahry_task.git
```

# Pre-requisites and Local Development
# Using Docker and Docker compose

The first step is to sign up for
a free account on [DockerHub](https://hub.docker.com/signup)  and then install the Docker desktop app on your local machine:
* [Docker for Mac](https://docs.docker.com/desktop/install/mac-install/)
* [Docker for Windows](https://docs.docker.com/desktop/install/windows-install/)
Once Docker is done installing we can confirm the correct version is running by typing the
command docker --version in the command line shell
```shell
$ docker --version
Docker version 20.10.14, build a224086
```
### Running our container
1- Open the project Code folder in Terminal/Windows (PowerShell).

2- Run this command .
```bash
docker-compose up -d --build
```

### To Stop the currently running container
Control+c (press the “Control” and “c” button at
the same time) and additionally type docker-compose down.
```shell
docker-compose down
```
### Now let’s confirm everything is working
```bash
docker-compose exec web python manage.py  makemigrations 
```
```bash
docker-compose exec web python manage.py  migrate 
```
> Now create the admin user
```bash
 docker-compose exec web python manage.py createsuperuser 
```
The application is run on http://127.0.0.1:8000/

**Open http://127.0.0.1:8000/api/v1 your web browser**

###  Set up your RDBMS , open your setting.py
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",  # set in docker-compose.yml
        "PORT": 5432,  # default postgres port
    }
}
```
<br/>
 All the extracted data is saved to the database to use it later if needed.
<br/>
<br/>

# Using virtual environment approach.
## To create a virtual environment 

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.

1- Open the project Code folder in Terminal/Windows (PowerShell).

2- Run this command .
```bash
# Windows
> python -m venv .venv
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# macOS
% python3 -m venv .venv
```

### To activate a new virtual environment called .venv:

```bash
# Windows
> .venv\Scripts\Activate.ps1
(.venv) >

# macOS
% source .venv/bin/activate
(.venv) %
```

### To deactivate and leave a virtual environment type deactivate.

```bash
# Windows
(.venv) > deactivate
>

# macOS
(.venv) % deactivate
%
```

### install requirements.txt


Run `pip install requirements.txt`. All required packages are included in the requirements file.

> make sure to activate the virtual environment first
```bash
pip install -r requirements.txt
```

**You might see a WARNING message about updating pip after running these commands. It’s always good to be on the latest version of software and to remove the annoying WARNING message each time you use pip. You can either copy and paste the recommended command or run `python -m pip install --upgrade pip` to be on the latest version.**

```bash
(.venv) > python -m pip install --upgrade pip
```

## Now let’s confirm everything is working by running Django’s internal web server via the runserver command

```bash
(.venv) > python manage.py  makemigrations 
```
```bash
(.venv) > python manage.py  migrate 
```
> Now create the admin user
```bash
(.venv) > python manage.py createsuperuser 
```
Run the surver
```bash
# Windows
(.venv) > python manage.py runserver

# macOS
(.venv) % python3 manage.py runserver
```

## Set up your RDBMS , open your setting.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_project_name',
        'USER': 'your_postgres_username',
        'PASSWORD': 'your_postgres_password',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '5432',
    }
}
```

Or you can stick the default database (sqlite3) but not recommended for Production. 

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

<br/>
All the extracted data is saved to the database to use it later if needed.
<br/>
The application is run on http://127.0.0.1:8000/ by default in the backend configuration.

**Open http://127.0.0.1:8000/api/v1 your web browser**

<br/>

# API Reference

## Getting Started
Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://127.0.0.1:8000/, which is in the backend configuration.

<br/>

## Endpoints

### POST /api/v1/
* General:
  * Creates a person record for the given national ID if it doesn't exists.
  * Returns a dictionary of the created record (national_id,birth_date,age,government,gender,century).
  * If a person record with e given national ID exists it return it without create a new one.

* `curl http://127.0.0.1:8000/api/v1/ -X POST -H "Content-Type: application/json" -d '{"nationalID" : 29608201301715}'`

```json
{
    "nationalID": 29608201301715,
    "birth_date": "20/08/1996",
    "age": 26,
    "government": "Sharqiya",
    "gender": "Male",
    "century": "Was Born in the century (1900-1999) "
}
```

### Validation Error
* Case 1:
    * If the given national ID is not 14 digits or a negative number.
    * It returns nationalID = National ID must be a 14 digits positive number.
* `curl http://127.0.0.1:8000/api/v1/ -X POST -H "Content-Type: application/json" -d '{"nationalID" : 12345}'`

```json
{
    "nationalID": [
        "National ID must be a 14 digits positive number"
    ]
}
```
* Case 2:
    * If the given national ID is not valid.
    * It returns nationalID = Enter a valid National ID.
* `curl http://127.0.0.1:8000/api/v1/ -X POST -H "Content-Type: application/json" -d '{"nationalID" : 59608201301715}'`

```json
{
    "nationalID": [
        "Enter a valid National ID"
    ]
}
```


## User Authentication (Extra)

added user authenticated so if we want to add permissions later id needed.

### GET /auth/users/
* General:
  * Create a new user.
  * Returns user information if it was created successfully.
* Sample: `curl http://127.0.0.1:8000/auth/users/ -X POST -H "Content-Type: application/json" -d '{"username": "testuser","email": "test@gmail.com","password": "MyPassword", "first_name": "test","last_name": "user"}'`

```json
{
    "id": 2,
    "username": "testuser",
    "email": "test@gmail.com",
    "first_name": "test",
    "last_name": "user"
}
```
<br/>

### POST /auth/jwt/create/
* General:
  * Login a user to the system by creating access and refresh tokens.
  * Returns user access and refresh tokens (to use it for logging-in) if it was created successfully.
* `curl http://127.0.0.1:8000/auth/jwt/create/ -X POST -H "Content-Type: application/json" -d '{"username": "testuser", "password": "MyPassword"}'`

```json
{
  {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NzY5NTY4NiwianRpIjoiZDI0MzkzNmM0MGFkNDcxMmEyNGI5N2M5YjIxNWI1ZjciLCJ1c2VyX2lkIjoxfQ.J_YiVMoPBuRK0qHSoLoOy8FrnPM0FFydztEu3qQ_Wy8",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3Njk1Njg2LCJqdGkiOiI5NTY4MGEyNjkyZDg0ZmJhOTlhNzU1NDhkZjQ5ZDc1NyIsInVzZXJfaWQiOjF9.AsdT7UfJTtXlkgKk3Xmhghz3Arz3yytU024wB25w-Nw"
}
}
```

>To keep your user logged-in , use an extention like [Moheader](https://modheader.com/)

- - - -
<br/>

# Deployment N/A

<br/>

# Authors
Omar Bendary
