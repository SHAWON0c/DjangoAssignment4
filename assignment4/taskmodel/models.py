from django.db import models
from django.utils import timezone

# Create your models here.
class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription= models.TextField()
    is_completed = models.BooleanField(default=False)
    Task_Assign_Date= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.taskTitle
