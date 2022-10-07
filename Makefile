APP = api

.PHONY: clean init

init: clean
	poetry env use python3.8 
	poetry install 
	poetry run pre-commit install

lint:
	poetry run flake8 ${APP} --max-line-length=120

analysis:
	poetry run bandit ${APP}

format:
	poetry run black ${APP}
	poetry run isort ${APP}

ci-bundle: analysis format lint