from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView

from app.forms import RegisterForm, UpdateUserForm, UserProfileInlineFormset, UpdateTaskForm
from app.models import ToDo


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
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['heading_text'] = 'Profile Info'
        context['finished_tasks'] = len(ToDo.objects.filter(todo_owner=self.request.user).filter(task_done=True))
        context['upcoming_tasks'] = len(ToDo.objects.filter(todo_owner=self.request.user).filter(task_done=False))
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
        return HttpResponseRedirect(self.get_success_url())


class TodoList(LoginRequiredMixin, ListView):
    model = ToDo
    template_name = 'taskmanager/todo.html'

    def get_queryset(self):
        return ToDo.objects.filter(todo_owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(TodoList, self).get_context_data(**kwargs)
        context['heading_text'] = 'My Tasks'
        context['tasks'] = self.get_queryset()
        return context


class ArchiveToDo(LoginRequiredMixin, ListView):
    model = ToDo
    template_name = 'taskmanager/archive-todo.html'

    def get_queryset(self):
        return ToDo.objects.filter(todo_owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ArchiveToDo, self).get_context_data(**kwargs)
        context['heading_text'] = 'Archive'
        context['tasks'] = self.get_queryset()
        return context


class CreateTodo(LoginRequiredMixin, CreateView):
    model = ToDo
    template_name = 'taskmanager/add-todo.html'
    success_url = reverse_lazy('todo')
    fields = ('task_name', 'task_text',)

    def get_context_data(self, **kwargs):
        context = super(CreateTodo, self).get_context_data(**kwargs)
        context['heading_text'] = 'Create Task'
        return context

    def form_valid(self, form):
        form.instance.todo_owner = self.request.user
        return super(CreateTodo, self).form_valid(form)


class UpdateToDo(LoginRequiredMixin, UpdateView):
    model = ToDo
    template_name = 'taskmanager/update-todo.html'
    success_url = reverse_lazy('todo')
    form_class = UpdateTaskForm

    def get_context_data(self, **kwargs):
        context = super(UpdateToDo, self).get_context_data(**kwargs)

        if self.request.POST:
            context['form'] = UpdateTaskForm(self.request.POST, instance=self.object)
        else:
            context['form'] = UpdateTaskForm(instance=self.object)
        context['heading_text'] = 'Edit Task'

        return context


@login_required
@csrf_exempt
def mark_as_done(request, pk):
    task = ToDo.objects.get(pk=pk)
    task.task_done = True
    task.save()
    return redirect('todo')


class DeleteTodo(LoginRequiredMixin, DeleteView):
    model = ToDo
    success_url = reverse_lazy('todo')

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)
