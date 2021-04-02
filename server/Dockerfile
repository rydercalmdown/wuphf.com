FROM python:3.7
WORKDIR /code
COPY src/requirements.txt .
RUN pip install -r requirements.txt
COPY src .
CMD [ "gunicorn", "--workers", "3", "-b", "0.0.0.0:8000", "wuphf.wsgi" ]
