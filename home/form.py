# Django
from django import forms
from froala_editor.widgets import FroalaEditor

# Owns
from .models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['content']