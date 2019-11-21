from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .models import Movie

from .forms import ReviewForm

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies,}
    return render(request, 'movies/index.html', context)

def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review_form = ReviewForm()
    reviews = movie.review_set.all()
    
    context = {'movie': movie, 'reviews': reviews, 'review_form': review_form}
    return render(request, 'movies/detail.html', context)