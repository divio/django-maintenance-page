# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from functools import partial

from aldryn_client import forms


class Form(forms.BaseForm):
    def to_settings(self, data, settings):
        from aldryn_addons.utils import djsenv
        from django_maintenance_page import conf

        env = partial(djsenv, settings=settings)

        if env('DJANGO_MODE') == 'build':
            return settings

        release_required = not env('STAGE') == 'local'
        release_identifier = env(conf.MAINTENANCE_ENV_VAR, required=release_required)
        migration_commands = settings.setdefault('MIGRATION_COMMANDS', [])
        migration_commands.insert(
            0,
            'python manage.py migrate --noinput django_maintenance_page',
        )
        migration_commands.insert(
            1,
            'python manage.py create_release {}'.format(release_identifier),
        )
        return settings
