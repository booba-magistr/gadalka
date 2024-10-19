#!/bin/sh

if [ "$POSTGRES_DB" = "gadalka"]
then
    while ! nc -z "db" $POSTGRES_PORT; do
        sleep 0.5
    done
fi

python manage.py makemigrations
python manage.py migrate

exec "$@"