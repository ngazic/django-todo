"""shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


app_name='todo' #namespace for this app
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:todo_list_id>', views.detail, name='detail'),
    path('<int:todo_list_id>/active-list', views.active_list, name='active_list'),
    path('<int:todo_list_id>/edit', views.edit, name='edit'),
]

"""
URL's for generic views would be: 


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.TodoListDetail.as_view(), name='detail'),
    path('<int:todo_list_id>/active-list', views.active_list, name='active_list'),
    path('<int:todo_list_id>/edit', views.edit, name='edit'),
]
"""
