from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView

from app.forms import RegisterForm, UpdateUserForm, UserProfileInlineFormset


def index(request):
    return render(request, 'index.html')


class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('home page')
    template_name = 'profile/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading_text'] = 'Register'
        return context

    def form_valid(self, form):
        data = super().form_valid(form)
        login(self.request, self.object)
        return data


class LoginUserView(LoginView):
    template_name = 'profile/login.html'
    redirect_authenticated_user = True

    def get_queryset(self):
        return User.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading_text'] = 'Log In'
        return context


class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'profile/profile-page.html'
    model = User
    context_object_name = 'account'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading_text'] = 'Profile Info'
        return context


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'profile/edit-profile.html'
    form_class = UpdateUserForm

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('profile account', kwargs={'pk': pk})

    def get_context_data(self, **kwargs):
        context = super(UpdateProfileView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['form'] = UpdateUserForm(self.request.POST, instance=self.object)
            context['user_profile_meta_formset'] = UserProfileInlineFormset(self.request.POST, instance=self.object)
        else:
            context['form'] = UpdateUserForm(instance=self.object)
            context['user_profile_meta_formset'] = UserProfileInlineFormset(instance=self.object)
        context['heading_text'] = 'Edit Profile'
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        user_profile = context['user_profile_meta_formset']
        if user_profile.is_valid():
            self.object = form.save()
            user_profile.instance = self.object
            user_profile.save()
        # return self.render_to_response(self.get_context_data(form=form))
        return HttpResponseRedirect(self.get_success_url())



