#! /bin/bash
#gunicorn main:app --workers 4 --timeout 120 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
uvicorn main:app --port 30080 --host 0.0.0.0
