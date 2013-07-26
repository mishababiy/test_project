MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=test_project.settings $(MANAGE) test test_project

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=test_project.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=test_project.settings $(MANAGE) syncdb --noinput
