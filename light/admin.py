# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Light
# Register your models here.

class LightAdmin(admin.ModelAdmin):
    list_display = ('id','state','color')
    list_editable = ('state','color')
    list_filter = ('state','color')









admin.site.register(Light, LightAdmin)
