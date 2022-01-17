from django.views.generic import DetailView
from django.http import HttpResponse
from django.views import generic
import todolist
from todolist.models import TodoList
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import TodoList
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils import timezone
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
    template = loader.get_template('todolist/new.html')
    return HttpResponse( template.render({}, request))
    

def post(request):
    if request.method == 'POST':
        tmp = todolist(user=request.user.username, Todolist_text=request.POST.get('Todolist_text'), TodoList_content=request.POST.get('TodoList_content'),TodoList_when=request.POST.get('TodoList_when'),TodoList_where = request.POST.get('TodoList_where'))
        tmp.save()
        return redirect('todolist:index')
    else:
        temp = TodoList.objects.all()
        return render(request, 'index.html', {'todolist:index'})

