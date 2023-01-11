# drs_twitter

This is a Django REST framework application. This application uses a precompiled database. Database values are provided to the user on the HTTP requests.

## Installation

1. Create virutal environment and install dependencies using requirements.txt
```py
# create virtual environment
python -m venv .env

# activte virtual environment
.env\Scripts\activate

# install dependecies
pip install -r requirements.txt
```
2. Provide config.env file with following details.
```
    1. SECRETE_KEY (secrete key)
    2. DB_ENGINE (database engine)
    3. DB_NAME (name of database)
    4. DB_USER (username of database user)
    5. DB_PASSWORD (password of database user)
    6. DB_HOST (url of database)
    7. DB_PORT (port of database)
```
3. Make migrations and migrate database.
```py
# make migrations
python manage.py makemigrations

# migrate database
python manage.py migrate

# create superuser
python manage.py createsuperuser
```
4. Start django server
```
python manage.py runserver
```

## License
MIT License

Copyright (c) 2023 Yashodhan Ketkar