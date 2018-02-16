# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DjangoMaintenancePageConfig(AppConfig):
    name = 'django_maintenance_page'
    verbose_name = _('Django Maintenance Page')
