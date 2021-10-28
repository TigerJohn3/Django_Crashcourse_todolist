from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm

# Create your views here.

def todo_list(request):
    todos = Todo.objects.all()
    print(todos)
    context = {
        "todo_list": todos
    }
    return render(request, "todo_list.html", context)

# CRUD - Create, Retrieve, Update, Delete, (List)

def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        "todo": todo
    }
    return render(request, "todo_detail.html", context)

def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        #name = form.cleaned_data['name']
        #due_date = form.cleaned_data['due_date']
        #new_todo = Todo.objects.create(name=name, due_date=due_date)
        return redirect('/')
    context = {"form": form}
    return render(request, "todo_create.html", context)

def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {"form": form}
    return render(request, "todo_update.html", context)

def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')
