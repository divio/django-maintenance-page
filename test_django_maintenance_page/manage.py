#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import os

from django.core.management import execute_from_command_line

os.environ['DJANGO_SETTINGS_MODULE'] = 'test_django_maintenance_page.settings'


if __name__ == "__main__":
    execute_from_command_line()
