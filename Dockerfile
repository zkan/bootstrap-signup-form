FROM python:3.7-alpine

RUN pip install pipenv

COPY . /app/
WORKDIR /app/
RUN pipenv install

ENTRYPOINT ["sh", "-c", "cd bootstrap_signup_form && pipenv run python manage.py migrate && pipenv run python manage.py runserver 0.0.0.0:8000"]
