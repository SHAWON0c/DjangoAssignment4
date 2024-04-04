from django.db import models
from taskmodel.models import TaskModel

# Your models for app1 go here


# Create your models here.
class TaskCategory(models.Model):
    categoryName= models.CharField(max_length=100)
    task = models.ManyToManyField(TaskModel)

    def __str__(self):
        return self.categoryName