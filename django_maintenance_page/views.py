# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.shortcuts import render
from django.views.defaults import server_error

from . import conf
from .models import Release


def handler500(request):
    if conf.MAINTENANCE_MODE or not(Release.is_up_to_date()):
        return render(request, 'maintenance.html', status=conf.MAINTENANCE_STATUS_CODE)
    return server_error(request)
