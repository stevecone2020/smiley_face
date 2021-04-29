from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from .models import TodoItem

# Create your views here.

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html',
        {'all_items' : all_todo_items})

def addTodo(request):
    try:
        new_item = TodoItem(content = request.POST['content'])
    except:
        return HttpResponseRedirect('/todo/')
    else:
        new_item.save()
        return HttpResponseRedirect('/todo/')

