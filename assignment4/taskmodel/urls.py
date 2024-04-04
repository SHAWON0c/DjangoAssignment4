from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.taskmodel, name='modelpage'),
    path('editModel/<int:id>/', views.edit_model, name='editmodel'),
     path('deleteModel/<int:id>/', views.delete_taskmodel, name='dltmodel'),

]
