# Django
from django.contrib import admin

# Owns
from .models import *

admin.site.register(BlogModel)
admin.site.register(Profile)
