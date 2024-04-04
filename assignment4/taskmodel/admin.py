from django.contrib import admin
from .models import *

__all__ = ['TaskModel']

admin.site.register(TaskModel)
