FROM python:slim

WORKDIR /home/posts/dlf

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY dlf.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP dlf.py

ENV PORT 8080
ENTRYPOINT ["./boot.sh"]

