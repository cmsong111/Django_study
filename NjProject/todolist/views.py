from django.views.generic import DetailView
from django.views import generic
from todolist.models import TodoList
from django.shortcuts import get_object_or_404, render
from .models import TodoList
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import TodolistForm
from django.contrib.auth import get_user_model

#from account.models import User

# Create your views here.

#def index(request):

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_todolist_list'

    def get_queryset(self):
        return TodoList.objects.order_by('TodoList_when')[:]

class todolistDetail(DetailView):
    template_name = 'detail.html'
    model = TodoList

class todolistedit(DetailView):
    template_name = 'edit.html'
    model = TodoList


def todolistnew(request):
    if request.method == 'POST':
        form = TodolistForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            #temp.user = user.username
            #temp.bool.. = true
            temp.save()
            return redirect('todolist:index')
    else:   
        form = TodolistForm()
    context = {'form': form }
    return render(request, 'new.html', context)