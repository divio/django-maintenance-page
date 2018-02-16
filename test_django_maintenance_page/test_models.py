# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.db.utils import IntegrityError
from django.test import TestCase

from django_maintenance_page.models import Release


class ReleaseTestCase(TestCase):
    def test_representation(self):
        release = Release.objects.create(identifier='v1.0')
        self.assertEquals('{}'.format(release), 'v1.0')

    def test_identifier_uniqueness(self):
        Release.objects.create(identifier='v1.0')
        Release.objects.create(identifier='v2.0')
        self.assertRaises(IntegrityError, Release.objects.create, identifier='v2.0')

    def test_get_current_identifier(self):
        self.assertEquals(Release.get_current_identifier(), '')

        Release.objects.create(identifier='v2.0')
        self.assertEquals(Release.get_current_identifier(), 'v2.0')

        Release.objects.create(identifier='v3.0')
        self.assertEquals(Release.get_current_identifier(), 'v3.0')

        Release.objects.create(identifier='v1.0')
        self.assertEquals(Release.get_current_identifier(), 'v1.0')
