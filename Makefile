.DEFAULT_GOAL := test

check_prereqs:
	bash -c '[[ -n $$VIRTUAL_ENV ]]'
	bash -c '[[ $$(python3 --version) == *3.8.9* ]]'

install: check_prereqs
	python3 -m pip install -e '.[dev]'
	pip install -r requirements.txt

install-dev: install
	pip install -r test_requirements.txt

# test
test: install
	pylint singer --extension-pkg-whitelist=ciso8601 -d missing-docstring,broad-except,bare-except,too-many-return-statements,too-many-branches,too-many-arguments,no-else-return,too-few-public-methods,fixme,protected-access
	nosetests --with-doctest -v
	py.test tests

# git
git-add:
	git add .

git-pre-commit:
	pre-commit install

git-commit:
	git commit -m "update"

push: git-add git-pre-commit git-commit
	git push origin master
