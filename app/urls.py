from django.contrib.auth.views import LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app import views
from app.views import RegisterView, LoginUserView, ProfileView, UpdateProfileView, TodoList

urlpatterns = [
                  path('', views.index, name='home page'),
                  path('register/', RegisterView.as_view(), name='register'),
                  path('login/', LoginUserView.as_view(), name='login'),
                  path('logout/', LogoutView.as_view(), name='logout'),
                  path('profile/<int:pk>', ProfileView.as_view(), name='profile account'),
                  path('update-profile/<int:pk>', UpdateProfileView.as_view(), name='change profile'),
                  path('todo/', TodoList.as_view(), name='todo'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
