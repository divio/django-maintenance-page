# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import distutils
import os

MAINTENANCE_MODE = bool(distutils.util.strtobool(os.environ.get('DJANGO_MAINTENANCE_MODE', '0')))
MAINTENANCE_ENV_VAR = os.environ.get('DJANGO_MAINTENANCE_ENV_VAR', 'DJANGO_MAINTENANCE_PAGE_RELEASE')
MAINTENANCE_STATUS_CODE = int(os.environ.get('DJANGO_MAINTENANCE_STATUS_CODE', '503'))
