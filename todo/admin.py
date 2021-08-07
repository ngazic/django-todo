from django.contrib import admin
from .models import TodoList, Product

# Register your models here.

admin.site.register(TodoList)
admin.site.register(Product)
