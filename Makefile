SELF_DIR=$(shell pwd)
UWSGI_PID=/tmp/sola-master.pid
VIRT=$(HOME)/.virtualenvs/sola
PYTHON=$(VIRT)/bin/python

uwsgi-restart: uwsgi-stop sleep uwsgi-start

uwsgi-start:
	$(VIRT)/bin/uwsgi \
		--chdir=$(SELF_DIR) \
		--env DJANGO_SETTINGS_MODULE=sola.settings \
		--socket=127.0.0.1:49153 \
		--module 'django.core.handlers.wsgi:WSGIHandler()' \
		--master \
		--pidfile=$(UWSGI_PID) \
		--processes=5 \
		--limit-as=128 \
		--max-requests=5000 \
		--vacuum \
		--home=$(VIRT)  \
		--pythonpath=$(SELF_DIR) \
		--daemonize=$(SELF_DIR)/../logs/uwsgi.log

uwsgi-reload:
	kill -HUP `cat $(UWSGI_PID)`

uwsgi-stop:
	kill -INT `cat $(UWSGI_PID)`

sleep:
	sleep 1

start:
	$(PYTHON) manage.py runserver

sync:
	$(PYTHON) manage.py syncdb
