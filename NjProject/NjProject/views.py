from pprint import pprint
from django.views.generic.base import TemplateView
from django.apps import apps

#--- TemplateView
class HomeView(TemplateView):

    template_name = 'NjProject/templates/home.html'