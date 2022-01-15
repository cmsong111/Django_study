from django.urls import path
from . import views


app_name = 'todolist'

urlpatterns = [
    #todolist/
    path('', views.IndexView.as_view(), name = 'index'),

    #todolist/new
    path('new/', views.todolistnew, name = 'new'),

    #todolist/99
    path('<int:pk>/', views.todolistDetail.as_view(), name = 'detail'),

    #todolist/99/edit
    path('<int:pk>/edit', views.todolistedit.as_view(), name = 'edit'),

]
