from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from todolist.models import TodoList
from django.shortcuts import get_object_or_404, render

#from account.models import User

# Create your views here.

#def index(request):

class todolistmodelView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['TodoList']
        #context = TodoList.objects.filter(user=User.get_username)
        return context


class todolistDetail(DetailView):
    template_name = 'detail.html'
    model = TodoList

