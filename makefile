.PHONY: install format lint typecheck test clean deploy

install:
	pip install -r requirements.txt

format:
	isort .
	black .

lint:
	pylint **/*.py
	flake8 .

typecheck:
	mypy .

test:
	python -m unittest discover tests

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".mypy_cache" -delete

deploy:
	pyinstaller --onefile --windowed --add-data "./src/data/config.json:." --add-data "chromedriver.exe:." ./src/main.py

all: install format lint typecheck test