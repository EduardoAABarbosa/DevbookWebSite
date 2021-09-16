from django.views.generic import TemplateView
from .models import Depoimentos

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['Testemunhos'] = Depoimentos.objects.all()
        return context