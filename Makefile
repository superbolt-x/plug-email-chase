.DEFAULT_GOAL := help
.PHONY: coverage install-test help format lint test push

# - init -
check-prereqs:
	python3 --version

install: check-prereqs
	if [ -f venv/bin/activate ]; then venv/bin/python3 -m pip install --upgrade pip && venv/bin/pip install -r requirements.txt ; else python -m pip install --upgrade pip && pip install -r requirements.txt; fi

install-test: check-prereqs
	if [ -f venv/bin/activate ]; then venv/bin/python3 -m pip install --upgrade pip && venv/bin/pip install -r test_requirements.txt ; else python -m pip install --upgrade pip && pip install -r test_requirements.txt; fi

# - format -
format: install-test  ## Black Format code PEP8
	black plug_email_chase

# - lint -
lint: install-test  ## Lint and static-check
	flake8 plug_email_chase
	pylint plug_email_chase --extension-pkg-whitelist=ciso8601 -d missing-docstring,broad-except,bare-except,too-many-return-statements,too-many-branches,too-many-arguments,no-else-return,too-few-public-methods,fixme,protected-access
	mypy plug_email_chase

# - test -
coverage: install-test  ## Run tests with coverage
	coverage erase
	coverage run --include=plug_email_chase/* -m pytest -ra
	coverage report -m

# - test -
test: install-test  ## Run tests
	py.test tests
	pytest -ra

# - git -
pre-commit:
	pre-commit install

commit:
	git add . && git commit -m "update"

push: pre-commit commit  ## Push code with tags
	git push && git push --tags

publish:  ## Publish to PyPi
	python3 setup.py sdist && twine upload --repository pypi -u $PYPI_USERNAME -p $PYPI_PASSWORD --skip-existing dist/*
