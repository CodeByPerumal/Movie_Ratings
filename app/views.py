from django.shortcuts import render
from app.forms import MoviesForm
from app.models import Movie


def index_view(request):
    return render(request, 'index.html')

def add_movie_view(request):
    form = MoviesForm()
    if request.method == 'POST':
        form = MoviesForm(request.POST)
        if form.is_valid():
            print('Form is valid printing movies...')
            form.save()
        else:
            print('Form is invalid', form.errors)
        return index_view(request)
    return render(request, 'add_movie.html', {'form' : form})

def list_movie_view(request):
    movies_list = Movie.objects.all().order_by('-rating')
    return render(request, 'list_movie.html', {'movies_list' : movies_list})