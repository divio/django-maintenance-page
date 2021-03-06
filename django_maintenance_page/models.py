# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import os

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from . import conf


@python_2_unicode_compatible
class Release(models.Model):
    identifier = models.CharField(_('Identifier'), max_length=127, unique=True)
    timestamp = models.DateTimeField(_('Timestamp'), auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-timestamp', )
        default_permissions = ''

    def __str__(self):
        return self.identifier

    @classmethod
    def get_current_identifier(cls):
        # 'Current' identifier is the last added one. This is NOT about version ordering.
        current_release = cls.objects.first()
        return current_release.identifier if current_release else ''  # To be compliant with empty (not unset) env vars

    @classmethod
    def is_up_to_date(cls):
        return cls.get_current_identifier() == os.environ.get(conf.MAINTENANCE_ENV_VAR, '')
