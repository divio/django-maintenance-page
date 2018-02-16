# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.contrib import admin

from .models import Release


class ReleaseAdmin(admin.ModelAdmin):
    search_fields = ('identifier', )
    list_filter = ('timestamp', )
    fields = ('identifier', 'timestamp', )
    list_display = fields
    readonly_fields = fields
    actions = None

    def has_add_permission(self, *args, **kwargs):
        return False

    def has_delete_permission(self, *args, **kwargs):
        return False


admin.site.register(Release, ReleaseAdmin)
