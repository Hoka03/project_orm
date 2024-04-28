from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from apps.to_do.models import ToDo
from apps.to_do.forms import ToDoForm


def home_page(request):
    todos = ToDo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todo_list.html', context)

#
# User.objects.create_user(username='Burildibek', password='1')
# User.objects.create_user(username='Qayrildibek', password='2')
# User.objects.create_user(username='Yeqildibek', password='3')


def add_todo_page(request):
    form = ToDoForm()
    context = {
        'form': form
    }
    return render(request, 'add_todo.html', context)


def add_todo(request):
    form = ToDoForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Todo added!!!')
    else:
        messages.error(request, form.errors)
    return redirect('add_todo_page')


def edit_page(request, pk):
    todos = ToDo.objects.get(id=pk)
    if request.method == 'POST':
        todos.title = request.POST.get('title')
        todos.description = request.POST.get('description')
        todos.done = request.POST.get('done') == 'on'
        done_at_str = request.POST.get('done_at')
        todos.done_at = request.POST.get(done_at_str)
        todos.start_date = request.POST.get('start_date')
        todos.end_date = request.POST.get('end_date')
        todos.save()
        return redirect('home_page')
    return render(request, 'edit_page.html', {'todos': todos})


def delete_page(request, pk):
    deletes = ToDo.objects.get(id=pk)
    context = {
        "deletes": deletes
    }
    if request.method == 'POST':
        deletes.delete()
        return redirect('home_page')
    return render(request, 'delete_page.html', context)