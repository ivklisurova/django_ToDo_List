from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from app.models import Profile


def index(request):
    return render(request, 'index.html')


class ProfileView(TemplateView):
    template_name = 'profile.html'
    profile_model = Profile

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['my_profile'] = self.profile_model.objects.get()
        return data


