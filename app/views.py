from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

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


class ProfileView(TemplateView):
    template_name = 'userprofile.html'
    profile_model = Profile

    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     data['my_profile'] = self.profile_model.objects.get()
    #     return data
