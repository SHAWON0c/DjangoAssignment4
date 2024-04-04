from django.shortcuts import render , redirect
from.forms import TaskCategoryForm
from.models import TaskCategory


# Create your views here.
def taskcategory(request):
   if request.method == 'POST':
        form = TaskCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorypage')
   else:
        form = TaskCategoryForm()
   return render(request, 'taskcategory.html', {'form': form})