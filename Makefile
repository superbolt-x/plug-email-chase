.DEFAULT_GOAL := test

check_prereqs:
	bash -c '[[ -n $$VIRTUAL_ENV ]]'
	bash -c '[[ $$(python3 --version) == *3.5.2* ]]'

install: check_prereqs
	python3 -m pip install -e '.[dev]'
	pip install -r requirements.txt && echo 'y' | pip3 uninstall pygoogle && pip3 install .

test: install
	pylint singer --extension-pkg-whitelist=ciso8601 -d missing-docstring,broad-except,bare-except,too-many-return-statements,too-many-branches,too-many-arguments,no-else-return,too-few-public-methods,fixme,protected-access
	nosetests --with-doctest -v
	py.test tests

push:
	git add . && git commit -m "update - $(date)" && git push origin master
