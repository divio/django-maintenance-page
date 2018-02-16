***********************
Django Maintenance Page
***********************

**Django Maintenance Page** Display a nice and automatic maintenance page when a server error occurs while deploy is running.


How does it work?
#################

Automatic maintenance mode
**************************

This project assumes:
1) You have some env var which defines the current release version on every server instance.
2) Your deploy routine creates new machines and replace the old ones by them (instead of updating the code directly on the very same machine).

So, for this example, lets assume machines are on version v1.0 (so release env var is v1.0) and you're about to deploy v1.1.

1) Create a new machine and set release env var to target version (v1.1) on it. Add it to your deploy routine (if you don't have it already).
2) Call ``python manage.py create_release`` on your new machine. Add it to your deploy routine.
3) Run deploy itself, with migrations, etc.
4) Replace the old machines (the ones stuck on v1.0) by the new ones (as you usually do).

| The automatic maintenance page would happen during step (3). If some user faces an error during your deploy, django_maintenance_page will check the target release (v1.1 on your database) against the current machine release (v1.0).
| Since they don't match we can presume this is a 'deploy error' - so display the maintenance page.
| In case they match (in other words every moment other than step (3)) the regular 5XX error will be served.

Manual maintenance mode
***********************

| Aside of the magic aforementioned you can serve the maintenance page when a server error occurs by setting ``DJANGO_MAINTENANCE_MODE=True`` env var.
| Note that this will affect only the 5XX errors. A successful request won't serve the maintenance page.


Installation and configuration
##############################

Via Divio Cloud
***************

* Add "Django Maintenance Page" addon
* Add ``handler500 = 'django_maintenance_page.views.handler500'`` to your ``urls.py``

Via pip (WIP)
*************

* ``pip install django-maintenance-page``
* Add ``django_maintenance_page`` to your ``INSTALLED_APPS``
* Run ``python manage.py migrate django_maintenance_page``
* Add ``handler500 = 'django_maintenance_page.views.handler500'`` to your ``urls.py``


Settings
########

============================ ===================================== =======================================================================
env var                      default                               description
---------------------------- ------------------------------------- -----------------------------------------------------------------------
DJANGO_MAINTENANCE_MODE      ``False``                             If set to True all server error requests will lead to maintenance page
DJANGO_MAINTENANCE_ENV_VAR   ``'DJANGO_MAINTENANCE_PAGE_RELEASE'`` Defines the env var to be used for Releases comparison
MAINTENANCE_STATUS_CODE      ``503``                               Defines the HTTP status code for maintenance response
============================ ===================================== =======================================================================


Local development
#################

* ``make setup``: Setup project for local development/tests
* ``make test``: Run test suite
* ``make test_server``: Run server with embedded test project
* ``make test_shell``: Run django shell with embedded test project
* ``tox``: Run multi-environment test suite
