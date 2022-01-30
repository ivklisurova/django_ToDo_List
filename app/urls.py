from django.urls import path
from django.views.generic import TemplateView

from app import views

urlpatterns = [
    path('', views.index, name='home page'),
    path('about/', TemplateView.as_view(template_name='profile.html'), name='profile')
]
