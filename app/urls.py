from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView

from app import views
from app.views import RegisterView, LoginUserView

urlpatterns = [
    path('', views.index, name='home page'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', TemplateView.as_view(template_name='profile/account.html'), name='accounts')
]
