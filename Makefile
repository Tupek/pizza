venv:
	python3 -m venv venv

install_deps:
	pip install -r requirements.txt

build:
	docker-compose up --force-recreate --build

up:
	docker-compose up

format:
	black . --exclude venv/

lint:
	flake8 .

mypy:
	mypy .
