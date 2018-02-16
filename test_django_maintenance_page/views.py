# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.http import HttpResponse


def broken_view(request):
    return 1 / 0


def working_view(request):
    return HttpResponse('OK!')
