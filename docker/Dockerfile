FROM python:3.12.4-slim-bullseye

WORKDIR /app
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# RUN pip install pyinstaller Pillow flake8 black isort mypy pylint 
COPY ./.flake8 .
COPY ./.vscode ./.vscode
COPY ./makefile .
COPY ./mypy.ini .

RUN apt-get update && apt-get install build-essential