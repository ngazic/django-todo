from typing import Generic
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from  django.http import HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Product, TodoList

# Create your views here.

def index(request):
    all_todos = TodoList.objects.order_by('name')
    context = {
        'all_todos': all_todos
    }
    return render(request,'todo/index.html',context=context)

"""
generic views would be sonething like this: 

class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'all_todos'
    
    def get_queryset(self):
        return TodoList.objects.order_by('name') 

class TodoListDetail(generic.DetailView):
    model = TodoList
    context_object_name = 'todo'
    template_name = 'todo/details.html'
"""

def detail(request, todo_list_id):
    todo = get_object_or_404(TodoList, pk=todo_list_id)
    return render(request,'todo/details.html', {'todo': todo})

def active_list(request, todo_list_id):
    todo = get_object_or_404(TodoList, pk=todo_list_id)
    return render(request,'todo/edit.html', {'todo': todo})

def edit(request, todo_list_id):
    todo = get_object_or_404(TodoList,pk=todo_list_id)
    all_products = todo.product_set.all().filter(done=False)
    print(all_products)
    
    checked_items = request.POST.getlist('done')
    try:
        
        for item in checked_items:
            # product = get_object_or_404(Product,pk=item)
            product = all_products.get(pk=item)
            product.done = True
            product.save()
            print(product)
    except (KeyError, Product.DoesNotExist):
        return render(request, 'todo/details.html', {
            'todo': todo,
            'error_message': "There was error while editing the list"})
    else:
        # return HttpResponse(request, 'all good')
        return HttpResponseRedirect(reverse('todo:index'))
    # print(request.POST)
    # print(type(done_items))
    # print(done_items)
    # print(request.POST['done1'])
    # return render(request, 'todo/edit.html', {'todo': todo})
        
