from django import forms

from .models import Environment


class EnvironmentForm(forms.ModelForm):
    year = forms.CharField(required=True, label="Année scolaire",
                           widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Environment
        exclude = ('name', )
