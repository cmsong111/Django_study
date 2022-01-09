from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views import generic
from todolist.models import TodoList
from django.shortcuts import get_object_or_404, render

#from account.models import User

# Create your views here.

#def index(request):


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_todolist_list'

    def get_queryset(self):
        """Return the last all published questions."""
        return TodoList.objects.order_by('-TodoList_when')[:]

class todolistDetail(DetailView):
    template_name = 'detail.html'
    model = TodoList

