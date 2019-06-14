FROM python:3.7

RUN pip install Django==2.2.2 \
                psycopg2==2.7.1

COPY . /app/
WORKDIR /app/
RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "-c", "cd bootstrap_signup_form && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
