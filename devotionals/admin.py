# -*- coding: utf-8 -*-
""" devotionals Admin """

from django.contrib import admin
from devotionals.models import Daily_Devotional


class Daily_DevotionalAdmin(admin.ModelAdmin):
    """ model admin that manages daily devotionals """
    pass


admin.site.register(Daily_Devotional, Daily_DevotionalAdmin)
