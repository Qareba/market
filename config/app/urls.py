from django.urls import path, include
from . import views

urlpatterns = [
    path('main/', views.CatalogListView.as_view(), name='main'),
    path('create/', views.CatalogCreateView.as_view(), name='create')
]
