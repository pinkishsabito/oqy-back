PIP=pip

install:
	# installation
	$(PIP) install -r requirements.txt

code:
	# code format
	black ./oqy

	# type check
	mypy ./oqy --ignore-missing-imports

	# lint check
	pylint ./oqy --rcfile=.pylintrc --load-plugins pylint_django --django-settings-module=api.settings

	# scan for errors
	# flake8 ./oqy

	# security check
	# bandit ./oqy

test:
	# unit tests
	# pytest ./oqy -vv

test-cov:
	# check coverage of unit tests
	# pytest --cov=oqy ./oqy

.PHONY: install code test test-cov
