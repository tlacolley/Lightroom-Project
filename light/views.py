# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy

import json
from django.http import HttpResponse, JsonResponse

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
    form_class = LightForm
    success_url = reverse_lazy('list_light')

    def form_valid(self, form):
        self.object = form.save()
        print self.object.state
        return JsonResponse({
            "id" : self.object.id,
            "state" : self.object.state,
        })
