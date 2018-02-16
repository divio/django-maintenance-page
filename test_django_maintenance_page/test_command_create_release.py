# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.core.management import call_command
from django.test import TestCase

from django_maintenance_page.models import Release

from .utils import override_env_vars, no_output


class CommandTestCase(TestCase):
    @no_output()
    def test_common(self):
        self.assertEquals(Release.objects.count(), 0)

        with override_env_vars(DJANGO_MAINTENANCE_PAGE_RELEASE='v1.0'):
            call_command('create_release')
        self.assertEquals(Release.objects.count(), 1)
        self.assertEquals(Release.objects.get().identifier, 'v1.0')

        with override_env_vars(DJANGO_MAINTENANCE_PAGE_RELEASE='v1.1'):
            call_command('create_release')
        self.assertEquals(Release.objects.count(), 2)

    @no_output()
    def test_var_not_set(self):
        self.assertEquals(Release.objects.count(), 0)

        with override_env_vars(DJANGO_MAINTENANCE_PAGE_RELEASE=''):
            self.assertRaises(AssertionError, call_command, 'create_release')
        self.assertEquals(Release.objects.count(), 0)

    @no_output()
    def test_duplicated_release(self):
        self.assertEquals(Release.objects.count(), 0)

        with override_env_vars(DJANGO_MAINTENANCE_PAGE_RELEASE='v1.0'):
            call_command('create_release')
            call_command('create_release')
        self.assertEquals(Release.objects.count(), 1)
        self.assertEquals(Release.objects.get().identifier, 'v1.0')
