#!/bin/bash
# this script is used to boot a Docker container

source venv/bin/activate

# options specify the file paths for the access log and error log files, respectively
exec gunicorn -b :8080 --access-logfile - --error-logfile - dlf:app
