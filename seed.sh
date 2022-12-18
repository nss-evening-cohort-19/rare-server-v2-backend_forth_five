#!/bin/bash
rm -rf rarev2api/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations rarev2api
python3 manage.py migrate rarev2api
python3 manage.py loaddata users
python3 manage.py loaddata posts
python3 manage.py loaddata categories
python3 manage.py loaddata reactions
python3 manage.py loaddata post_reactions
python3 manage.py loaddata tags
python3 manage.py loaddata post_tags
python3 manage.py loaddata comments
