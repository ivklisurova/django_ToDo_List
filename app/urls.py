from django.urls import path
from django.views.generic import TemplateView

from app import views
from app.views import RegisterView

urlpatterns = [
    path('', views.index, name='home page'),
    path('register/', RegisterView.as_view(), name='register')
    # path('profile/', TemplateView.as_view(template_name='userprofile.html'), name='profile')
]
