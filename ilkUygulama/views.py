from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class AnasayfaSayfaGorunumu(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'anasayfa.html', context=None)

class HakkimdaSayfaGorunumu(TemplateView):
    template_name="hakkimda.html"

class IletisimSayfaGorunumu(TemplateView):
    template_name = 'iletisim.html'