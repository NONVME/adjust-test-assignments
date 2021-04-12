PROJECTNAME=$(shell basename "$(PWD)")

#Make пишет работу в консоль Linux. Сделаем его silent.
MAKEFLAGS += --silent

## Install dependencies
install:
	@poetry install

## run: Run production server
run:
	gunicorn config.wsgi --log-file -

## run-dev: Run developer server
run-dev:
	@poetry run python manage.py runserver

## lint: Run Flake8 linter
lint:
	@poetry check
	@poetry run flake8

## migrate: migrate
migrate:
	@poetry run python3 manage.py migrate

## test: Run tests
test: lint
	@poetry run coverage run --source='.' manage.py test

test-coverage-report:
	@poetry run coverage report -m $(ARGS)
	@poetry run coverage erase

test-coverage-report-xml:
	@poetry run coverage xml

heroku_release:
	python manage.py migrate

.PHONY: help
all: help
help: Makefile
	@echo
	@echo " Choose a command run in "$(PROJECTNAME)":"
	@echo
	@sed -n 's/^##//p' $< | column -t -s ':' |  sed -e 's/^/ /'
	@echo
