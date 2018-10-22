# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Light
from .forms import LightForm
# Create your views here.



class LightListView(ListView):
    model = Light

    def get_context_data(self, **kargs):
        context = ListView.get_context_data(self, **kargs)
        context["lights"] = []

        for light in self.get_queryset():
            context["lights"].append({
            "light" : light,
            "form" : LightForm(instance=light)

            })

        return context


class LightSwitchView(UpdateView):
    model = Light
    fields = ["state"]

    def get_success_url(self):
        return reverse('list_light')
