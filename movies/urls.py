from django.contrib import admin
from django.urls import path
from movies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('movies/', views.movies, name='movies_list'),
    path('movies/add', views.add, name='add_movie'),
    path('movies/<int:id>', views.detail, name='movie_detail'),
    path('movies/delete/<int:id>', views.delete, name='delete_movie'),  # Added delete URL pattern
]
