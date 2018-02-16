# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import os

from django.core.management.base import BaseCommand

from ... import conf
from ...models import Release


class Command(BaseCommand):
    def handle(self, *args, **options):
        identifier = os.environ.get(conf.MAINTENANCE_ENV_VAR, '').strip()
        assert identifier, 'Release identifier not found. Please set "{}" env var.'.format(conf.MAINTENANCE_ENV_VAR)

        if Release.objects.filter(identifier=identifier).exists():
            self.stderr.write('WARNING: Release already set to "{}".'.format(identifier))
            return

        Release.objects.create(identifier=identifier)
        self.stdout.write('Release set to "{}"'.format(identifier))
