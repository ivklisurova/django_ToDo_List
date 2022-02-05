from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView

from app.forms import RegisterForm, UpdateProfileForm
from app.models import Profile


def index(request):
    return render(request, 'index.html')


class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('home page')
    template_name = 'profile/register.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['heading_text'] = 'Register'
        return data


class LoginUserView(LoginView):
    template_name = 'profile/login.html'
    redirect_authenticated_user = True

    def get_queryset(self):
        return User.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['heading_text'] = 'Log In'
        return data


class ProfileView(DetailView, LoginRequiredMixin):
    template_name = 'profile/profile-page.html'
    model = User
    context_object_name = 'account'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['heading_text'] = 'Profile Info'
        return data







# class UpdateProfileView(UpdateView):
#     model = Profile
#     template_name = 'profile/edit_profile.html'
#     form_class = UpdateProfileForm
#     success_url = reverse_lazy('home page')
#
#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)
#         data['heading_text'] = 'Edit Profile'
#         data['form'] = self.form_class(instance=self.object)
#         return data
