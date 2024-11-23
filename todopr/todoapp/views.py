from django.shortcuts import render
from .forms import TodoForm                                             #adminusername:jishnusjyothish password:1
from .models import Todo
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()  
            
    else:
        form = TodoForm()

    tasks = Todo.objects.all() 
    return render(request, 'index.html', {'tasks': tasks, 'form': form})