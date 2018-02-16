# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.conf.urls import url

from .views import broken_view, working_view

handler500 = 'django_maintenance_page.views.handler500'

urlpatterns = [
    url(r'^broken/', broken_view, name='broken-view'),
    url(r'^working/', working_view, name='working-view'),
]
