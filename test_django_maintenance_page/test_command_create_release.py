# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.core.management import CommandError, call_command
from django.test import TestCase

from django_maintenance_page.models import Release

from .utils import no_output


class CommandTestCase(TestCase):
    @no_output()
    def test_common(self):
        self.assertEquals(Release.objects.count(), 0)

        call_command('create_release', 'v1.0')
        self.assertEquals(Release.objects.count(), 1)
        self.assertEquals(Release.objects.get().identifier, 'v1.0')

        call_command('create_release', 'v1.1')
        self.assertEquals(Release.objects.count(), 2)

    @no_output()
    def test_release_identifier_not_provided(self):
        self.assertEquals(Release.objects.count(), 0)

        self.assertRaises(CommandError, call_command, 'create_release')
        self.assertEquals(Release.objects.count(), 0)

    @no_output()
    def test_release_identifier_provided_multiple_times(self):
        self.assertEquals(Release.objects.count(), 0)

        self.assertRaises(CommandError, call_command, 'create_release', 'v1.0', 'v1.1')
        self.assertEquals(Release.objects.count(), 0)

    @no_output()
    def test_duplicated_release(self):
        self.assertEquals(Release.objects.count(), 0)

        call_command('create_release', 'v1.0')
        call_command('create_release', 'v1.0')
        self.assertEquals(Release.objects.count(), 1)
        self.assertEquals(Release.objects.get().identifier, 'v1.0')
