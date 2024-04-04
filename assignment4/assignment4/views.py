from django.shortcuts import render
from taskmodel.models import TaskModel
from taskcategory.models import TaskCategory

def home(request):
    # Query data from TaskModel and TaskCategory
    task_models = TaskModel.objects.all()
    task_categories = TaskCategory.objects.all()

    # Zip data together
    zipped_data = zip(task_models, task_categories)

    # Pass zipped data to the template
    return render(request, 'home.html', {'zipped_data': zipped_data})
