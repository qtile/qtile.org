#!/usr/bin/env bash
set -eo pipefail

# The post_compile hook is run by heroku-buildpack-python

echo "-----> Running release process"

# Install front-end dependencies
echo "-----> Installing front-end components"
bower install --config.interactive=false

# Compile static assets
echo "-----> Collecting static files"
python manage.py collectstatic --noinput --traceback 2>&1 | sed '/^Copying/d;/^$/d;/^ /d'

echo "-----> Compressing static files"
python manage.py compress --traceback 2>&1

echo "-----> Creating screenshot thumbnails"
python manage.py process_screenshots --traceback 2>&1

echo "-----> Release process done"
