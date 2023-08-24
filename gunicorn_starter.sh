#!/bin/sh

python3 run_migration.py

gunicorn --worker-class uvicorn.workers.UvicornWorker --workers 4  --bind 0.0.0.0:8000 --log-level info app.asgi:app