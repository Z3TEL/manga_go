from django.forms import ClearableFileInput
from django import forms
from .models import *

from django.forms import ClearableFileInput
...
class FeedModelForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['text']

class FileModelForm(forms.ModelForm):
    class Meta:
        model = PageFile
        fields = ['file']
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True}),
        }