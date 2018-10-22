from django import forms
from .models import Light


class LightForm(forms.ModelForm):
    class Meta:
        model = Light
        fields = "__all__"
