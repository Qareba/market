from django.shortcuts import render
from . import models
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.list import ListView


class CatalogListView(ListView):
    model = models.Catalog
    template_name = 'main.html'
    context_object_name = 'catalogs'

class CatalogCreateView(CreateView):
    model = models.Catalog
    fields = '__all__'
    template_name = 'create_form.html'
    success_url = reverse_lazy('main')



