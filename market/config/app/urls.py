from django.urls import path, include
from . import views

urlpatterns = [
   path('delete/<int:pk>', views.DeleteView.as_view(), name = 'delete'),
   path('update/<int:pk>', views.UpdateView.as_view(), name = 'update')
]
