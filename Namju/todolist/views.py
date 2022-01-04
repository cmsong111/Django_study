from typing import ContextManager
from django.shortcuts import render

from Namju import todolist
from django.views.generic import TemplateView
from django.views.generic import DeleteView
from todolist.models import TodoList



# Create your views here.

class todolistModelsView(TemplateView):
    template_name = 'todolist/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['TodoList']
        return super().get_context_data(**kwargs)
