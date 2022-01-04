from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'todolist'
URLPattern = [

    #/todolist
    path('',views.todolistModelsView.as_view(), name = 'index'),

]