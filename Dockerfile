FROM python:3.6-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /tecnoelectrocomercioonline

COPY requirements.txt /tecnoelectrocomercioonline/
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]