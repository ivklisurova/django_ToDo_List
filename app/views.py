from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView

from app.forms import RegisterForm
from app.models import Profile


def index(request):
    return render(request, 'index.html')


class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('home page')
    template_name = 'profile/register.html'


class LoginUserView(LoginView):
    template_name = 'profile/login.html'
    redirect_authenticated_user = True

    def get_queryset(self):
        return User.objects.filter(user=self.request.user)


class ProfileView(DetailView, LoginRequiredMixin):
    template_name = 'profile/account.html'
    model = Profile
    context_object_name = 'account'
    queryset = Profile.objects.get(user_id=5)
