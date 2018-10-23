# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Light(models.Model):
    LIGHT_CHOICE=(
    ('ON','Allume'),
    ('OFF','Eteint')
    )
    COLOR_CHOICE=(
    ('WHITE','white'),
    ('RED','red'),
    ('BLUE','blue'),
    ('GREEN','green'),
    ('YELLOW','yellow'),
    ('PURPLE','purple'),
    )
    state = models.CharField(max_length=10, choices=LIGHT_CHOICE, default='OFF')
    color = models.CharField(max_length=15, choices=COLOR_CHOICE, default='WHITE')



    def __unicode__(self):
        return "Light #%s [%s],[%s]" %(self.id, self.state, self.color)
