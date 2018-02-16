# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from imp import reload
import os
import sys

from contextlib2 import ContextDecorator

import django_maintenance_page.conf


class DevNull(object):
    def write(self, data):
        pass


class override_env_vars(ContextDecorator):
    def __init__(self, **replacement_env_vars):
        super(override_env_vars, self).__init__()
        self.replacement_env_vars = replacement_env_vars

    def __enter__(self):
        self.old_environ = os.environ.copy()
        os.environ.update(self.replacement_env_vars)
        reload(django_maintenance_page.conf)
        return self

    def __exit__(self, *exc):
        os.environ = self.old_environ
        reload(django_maintenance_page.conf)
        return False


class no_output(ContextDecorator):
    def __enter__(self):
        self.old_stdout = sys.stdout
        sys.stdout = DevNull()
        self.old_stderr = sys.stderr
        sys.stderr = DevNull()
        return self

    def __exit__(self, *exc):
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr
        return False
