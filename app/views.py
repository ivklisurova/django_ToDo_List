from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


def index(request):
    return render(request, 'index.html')


class ProfileView(TemplateView):
    template_name = 'profile.html'
