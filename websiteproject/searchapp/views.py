from django.shortcuts import render
from websiteapp.models import Movies
from  django.db.models import Q
# Create your views here.

# def SearchResult(request):
#     movies=None
#     query=None
#     if 'q' in request.GET:
#         query= request.GET.get('q')
#         movies=Movies.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
#     return render(request,'search.html',{'query':query,'movies':movies})


from django.shortcuts import render
from websiteapp.models import Movies
from .forms import SearchForm

from django.shortcuts import render
from websiteapp.models import Movies
from .forms import SearchForm

def movie_search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            movies = Movies.objects.filter(title__icontains=query)
            return render(request, 'movies/search_results.html', {'movies': movies, 'query': query})
    else:
        form = SearchForm()
    return render(request, 'movies/search.html', {'form': form})

# def movie_search(request):
#     if request.method == 'GET':
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             query = form.cleaned_data.get('query')
#             movies = Movies.objects.filter(title__icontains=query)
#             return render(request, 'movies/search_results.html', {'movies': movies, 'query': query})
#     else:
#         form = SearchForm()
#     return render(request, 'movies/search.html', {'form': form})