from pprint import pprint
from django.views.generic.base import TemplateView
from django.apps import apps

#--- TemplateView
class HomeView(TemplateView):

    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['todolist']
        return context