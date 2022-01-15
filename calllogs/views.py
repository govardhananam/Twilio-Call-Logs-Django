from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .services import get_logs

class GetLogs(TemplateView):
    template_name = 'logs.html'
    def get_context_data(self, *args, **kwargs):
        context = {
            'logs' : get_logs(),
        }
        return context
