from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Movie

def movies(request):
    data = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': data})

def home(request):
    return HttpResponse('Home page')

def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': data})

def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        year = request.POST.get('year')

        if title and year:
            movie = Movie(title=title, year=year)
            movie.save()
            return HttpResponseRedirect('/movies')  # Redirect to movie list after saving

    return render(request, 'movies/add.html')  # Display form if not POST

def delete(request, id):
    try:
        movie = Movie.objects.get(pk=id)
        movie.delete()  # Delete the movie
    except Movie.DoesNotExist:
        pass  # If the movie doesn't exist, do nothing
    return HttpResponseRedirect('/movies')  # Redirect to movie list after deletion
