from django.urls import path
from . import views


app_name = 'todolist'

urlpatterns = [
    #todolist/
    path('', views.todolistmodelView.as_view(), name = 'index'),
    
    #todolist/99
    #path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
]
