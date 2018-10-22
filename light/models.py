# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Light(models.Model):
    LIGHT_CHOICE=(
    ('ON','Allume'),
    ('OFF','Eteint')
    )
    state = models.CharField(max_length=10, choices=LIGHT_CHOICE, default='OFF')

    def __unicode__(self):
        return "Light #%s [%s]" %(self.id, self.state)
