# from django.shortcuts import render , redirect
# from.forms import TaskModelForm
# from.models import TaskModel
# from .import forms
# from . import models

# # Create your views here.
# def taskmodel(request):
#     if request.method == 'POST':
#          task_model_from = TaskModelForm(request.POST)
#          if task_model_from.is_valid():
#               task_model_from.save()
#               return redirect('modelpage')
#     else:
#          task_model_from = TaskModelForm()
         
#     return render(request,'taskmodel.html',{'form':task_model_from})


# def edit_model(request , id ):
#      file = models.TaskModel.objects.get(pk=id)
#      model_form=forms.TaskModelForm(instance=file)
#      if request.method == 'POST':
#          model_form=forms.TaskModelForm(request.POST ,instance=file)
#          if model_form.is_valid():
#               model_form.save()
#               return redirect('homepage')

          
#      return render(request, 'taskmodel.html', {'form': model_form} , )


# def delete_album(request):
#      file = models.TaskModel.objects.get(pk=id)
#      file.delete()
#      return redirect('homepage')

from django.shortcuts import render, redirect
from .forms import TaskModelForm
from .models import TaskModel

def taskmodel(request):
    if request.method == 'POST':
        task_model_form = TaskModelForm(request.POST)
        if task_model_form.is_valid():
            task_model_form.save()
            return redirect('modelpage')
    else:
        task_model_form = TaskModelForm()
    return render(request, 'taskmodel.html', {'form': task_model_form})

def edit_model(request, id):
    task_model_instance = TaskModel.objects.get(pk=id)
    if request.method == 'POST':
        model_form = TaskModelForm(request.POST, instance=task_model_instance)
        if model_form.is_valid():
            model_form.save()
            return redirect('homepage')
    else:
        model_form = TaskModelForm(instance=task_model_instance)
    return render(request, 'taskmodel.html', {'form': model_form})

def delete_taskmodel(request, id):
    task_model_instance = TaskModel.objects.get(pk=id)
    task_model_instance.delete()
    return redirect('homepage')
