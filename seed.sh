#!/bin/bash
rm -rarev2/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations rarev2api
python3 manage.py migrate rarev2api
python3 manage.py loaddata users
