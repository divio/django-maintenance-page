# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import requests

from django.core.urlresolvers import reverse
from django.test import LiveServerTestCase

from django_maintenance_page.models import Release

from .utils import override_env_vars


class Handler500TestCase(LiveServerTestCase):
    def assertWorkingViewReturned(self, response):
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content.decode('utf-8'), 'OK!')

    def assertDefault5XXReturned(self, response):
        self.assertEquals(response.status_code, 500)
        self.assertIn('<h1>Server Error (500)</h1>', response.content.decode('utf-8'))

    def assertCustom5XXReturned(self, response, status_code=503, content='Temporarily Down for Maintenance'):
        self.assertEquals(response.status_code, status_code)
        self.assertIn(content, response.content.decode('utf-8'))

    def test_request_ok(self):
        Release.objects.create(identifier='v1.0')

        with override_env_vars(DJANGO_MAINTENANCE_MODE='0', DJANGO_MAINTENANCE_PAGE_RELEASE='v1.0'):
            response = requests.get(self.live_server_url + reverse('working-view'))
        self.assertWorkingViewReturned(response)

        with override_env_vars(DJANGO_MAINTENANCE_MODE='0', DJANGO_MAINTENANCE_PAGE_RELEASE='v2.0'):
            response = requests.get(self.live_server_url + reverse('working-view'))
        self.assertWorkingViewReturned(response)

        with override_env_vars(DJANGO_MAINTENANCE_MODE='1', DJANGO_MAINTENANCE_PAGE_RELEASE='v1.0'):
            response = requests.get(self.live_server_url + reverse('working-view'))
        self.assertWorkingViewReturned(response)

        with override_env_vars(DJANGO_MAINTENANCE_MODE='1', DJANGO_MAINTENANCE_PAGE_RELEASE='v2.0'):
            response = requests.get(self.live_server_url + reverse('working-view'))
        self.assertWorkingViewReturned(response)

    def test_request_nok(self):
        Release.objects.create(identifier='v1.0')

        with override_env_vars(DJANGO_MAINTENANCE_MODE='0', DJANGO_MAINTENANCE_PAGE_RELEASE='v1.0'):
            response = requests.get(self.live_server_url + reverse('broken-view'))
        self.assertDefault5XXReturned(response)

        with override_env_vars(DJANGO_MAINTENANCE_MODE='0', DJANGO_MAINTENANCE_PAGE_RELEASE='v2.0'):
            response = requests.get(self.live_server_url + reverse('broken-view'))
        self.assertCustom5XXReturned(response)

        with override_env_vars(DJANGO_MAINTENANCE_MODE='1', DJANGO_MAINTENANCE_PAGE_RELEASE='v1.0'):
            response = requests.get(self.live_server_url + reverse('broken-view'))
        self.assertCustom5XXReturned(response)

        with override_env_vars(DJANGO_MAINTENANCE_MODE='1', DJANGO_MAINTENANCE_PAGE_RELEASE='v2.0'):
            response = requests.get(self.live_server_url + reverse('broken-view'))
        self.assertCustom5XXReturned(response)

    def test_request_nok_custom_status_code(self):
        Release.objects.create(identifier='v1.0')

        with override_env_vars(DJANGO_MAINTENANCE_PAGE_RELEASE='v2.0'):
            response = requests.get(self.live_server_url + reverse('broken-view'))
        self.assertCustom5XXReturned(response)

        with override_env_vars(DJANGO_MAINTENANCE_STATUS_CODE='502', DJANGO_MAINTENANCE_PAGE_RELEASE='v2.0'):
            response = requests.get(self.live_server_url + reverse('broken-view'))
        self.assertCustom5XXReturned(response, status_code=502)
