from django.contrib import admin
from .models import *

__all__ = ['TaskCategory']

admin.site.register(TaskCategory)
