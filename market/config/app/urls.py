from django.urls import path, include
from . import views

urlpatterns = [
   path('delete/<int:pk>', views.DeleteView.as_view(), name = 'delete'),
   path('update/<int:pk>', views.UpdateView.as_view(), name = 'update'),
   path('main/', views.CatologListView.as_view(), name='main'),
   path('create/', views.CatalogCreateView.as_view(), name='create')
]
