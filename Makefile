# django-simple-help
# Makefile

MANAGE=$(PWD)/tmp/$(PROJECT_NAME)/manage.py

docs:
	rst2html README.rst > index.html && zip docs.zip index.html

clear:
	rm -rf index.html docs.zip build dist django_simple_help.egg-info tmp

build:
	./setup.py bdist_wheel sdist

upload:
	./setup.py bdist_wheel sdist upload

create-virtualenv:
	virtualenv tmp/.env/`arch`

pip-install:
	pip install Django

startproject:
	cd tmp && django-admin.py startproject $(PROJECT_NAME)

makemessages:
	cd $(PROJECT_NAME);\
	for locale in `ls locale`; do\
		$(MANAGE) makemessages --locale=$$locale --extension=py,html,txt;\
	done

compilemessages:
	$(MANAGE) compilemessages
