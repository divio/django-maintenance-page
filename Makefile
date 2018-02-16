setup:
	python setup.py develop
	pip install "Django>1.8,<2.0"
	pip install -r requirements_test.txt
	test_django_maintenance_page/manage.py migrate

test:
	pytest --cov=django_maintenance_page --cov-config=.coveragerc test_django_maintenance_page/

test_server:
	test_django_maintenance_page/manage.py runserver

test_shell:
	test_django_maintenance_page/manage.py shell
