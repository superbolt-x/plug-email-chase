.DEFAULT_GOAL := help
.PHONY: coverage deps help lint push test

# - init -
check-prereqs:
	bash -c '[[ $$(python3 --version) == *3.8.9* ]]'

install: check-prereqs
	if [ -f venv/bin/activate ]; then venv/bin/python3 -m pip install --upgrade pip && venv/bin/pip install -r requirements.txt ; else python -m pip install --upgrade pip && pip install -r requirements.txt; fi

install-test: check-prereqs
	if [ -f venv/bin/activate ]; then venv/bin/python3 -m pip install --upgrade pip && venv/bin/pip install -r test_requirements.txt ; else python -m pip install --upgrade pip && pip install -r test_requirements.txt; fi

# - lint -
lint:  ## Lint and static-check
	flake8 plug_email_chase
	pylint plug_email_chase
	mypy plug_email_chase

# - test -
coverage: install  ## Run tests with coverage
	coverage erase
	coverage run --include=podsearch/* -m pytest -ra
	coverage report -m

test: install  ## Run tests
	pylint plug_email_chase --extension-pkg-whitelist=ciso8601 -d missing-docstring,broad-except,bare-except,too-many-return-statements,too-many-branches,too-many-arguments,no-else-return,too-few-public-methods,fixme,protected-access
	nosetests --with-doctest -v
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
