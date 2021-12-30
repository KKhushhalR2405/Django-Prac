from django import forms
from django.core import validators
from django.forms.models import fields_for_model


def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name needs to start with Z")

class FormName(forms.Form):
    name = forms.CharField(validators = [validators.MaxLengthValidator(6),
                                            check_for_z,])
    email = forms.EmailField(required=False)
    text = forms.CharField(widget=forms.Textarea)

