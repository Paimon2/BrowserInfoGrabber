FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN mkdir -p /app

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=main.py

CMD flask run -h 0.0.0.0 -p 80
