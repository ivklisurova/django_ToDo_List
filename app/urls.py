from django.contrib.auth.views import LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app import views
from app.views import RegisterView, LoginUserView, ProfileView, UpdateProfileView, TodoList, DeleteTodo, CreateTodo, \
    UpdateToDo, ArchiveToDo

urlpatterns = [
                  path('', views.index, name='home page'),
                  path('register/', RegisterView.as_view(), name='register'),
                  path('login/', LoginUserView.as_view(), name='login'),
                  path('logout/', LogoutView.as_view(), name='logout'),
                  path('profile/<int:pk>', ProfileView.as_view(), name='profile account'),
                  path('update-profile/<int:pk>', UpdateProfileView.as_view(), name='change profile'),
                  path('todo/', TodoList.as_view(), name='todo'),
                  path('archive/', ArchiveToDo.as_view(), name='archive'),
                  path('delete/<int:pk>', DeleteTodo.as_view(), name='delete todo'),
                  path('add/', CreateTodo.as_view(), name='create todo'),
                  path('mark-done/<int:pk>', views.mark_as_done, name='mark as done'),
                  path('edit/<int:pk>', UpdateToDo.as_view(), name='update todo'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
