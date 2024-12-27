from django.shortcuts import render
from . import models
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class DeleteView(DeleteView):
    model = models.Catalog
    template_name = "confirm_del.html"
    success_url = reverse_lazy('main')

class UpdateView(UpdateView):
    model = models.Catalog
    fields = '__all__'
    template_name = "create_form.html"
    success_url = reverse_lazy('main')