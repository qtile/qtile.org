#!/bin/bash

# 1. Collect static files
python manage.py collectstatic --noinput

# 2. Compress CSS/JS
python manage.py compress

# 3. Start the web server
newrelic-admin run-program gunicorn qtile.wsgi:application --bind=0.0.0.0:$PORT --workers=4 --log-level=info
