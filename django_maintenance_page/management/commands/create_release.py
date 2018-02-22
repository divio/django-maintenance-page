# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.core.management.base import BaseCommand

from ...models import Release


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('release_identifier')

    def handle(self, *args, **options):
        identifier = options['release_identifier'].strip()

        if Release.objects.filter(identifier=identifier).exists():
            self.stderr.write('WARNING: Release already set to "{}".'.format(identifier))
            return

        Release.objects.create(identifier=identifier)
        self.stdout.write('Release set to "{}"'.format(identifier))
