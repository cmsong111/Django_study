from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from todolist.models import TodoList


# Create your views here.

#def index(request):

class todolistmodelView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['TodoList']
        #context = TodoList.objects.filter(id=1)
        return context


class todolistDetail(ListView):
    model = TodoList
