#!/bin/bash


set -e
set -o pipefail # if any code doesn't return 0, exit the script

function start_server() {
  if [[ $ENVIRONMENT == "production" ]]; then
    echo Starting Gunicorn server..
    exec gunicorn settings.wsgi:application \
      --bind 0.0.0.0:8000 \
      --workers 3
  else
    echo Starting Django development server..
    python manage.py runserver 0.0.0.0:8000

  fi
}

start_server

exit 0
