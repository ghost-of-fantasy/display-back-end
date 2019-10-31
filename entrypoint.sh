#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

## 这该死的删库命令
#python manage.py flush --no-input
celery -A display worker -l info &
python3 manage.py makemigrations
python manage.py migrate
python manage.py initadmin
python manage.py collectstatic --no-input --clear

exec "$@"
