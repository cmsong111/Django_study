from django.urls import path
from . import views


app_name = 'todolist'

urlpatterns = [
    #todolist/
    path('', views.IndexView.as_view(), name = 'index'),
    
    #todolist/99
    path('<int:pk>/', views.todolistDetail.as_view(), name = 'detail'),
]
