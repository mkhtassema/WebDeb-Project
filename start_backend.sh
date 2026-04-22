#!/bin/bash
# Start Django backend
cd "$(dirname "$0")/filmspace_backend"
source venv/bin/activate
python manage.py runserver 8000
