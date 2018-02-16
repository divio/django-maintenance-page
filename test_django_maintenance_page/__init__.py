# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from os import environ
import django

environ['DJANGO_SETTINGS_MODULE'] = 'test_django_maintenance_page.settings'

django.setup()
