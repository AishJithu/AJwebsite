from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . models import Movies,Category,review
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from .forms import MovieForm
from django.contrib.auth.models import User
# Create your views here.



def allmovieCat(request,c_slug=None):
    c_page=None
    movies_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        movies_list=Movies.objects.all().filter(category=c_page)
    else:
        movies_list=Movies.objects.all()
    paginator=Paginator(movies_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        movies=paginator.page(page)
    except(EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_pages)

    return render(request,'user.html',{'category':c_page,'movies':movies})

def MovieDetail(request,movie_slug,c_slug,):
    try:
        movie=Movies.objects.get(category__slug=c_slug,slug=movie_slug)
    except Exception as e:
        raise e
    return render(request,'movie.html',{'movie':movie})

def addmovie(request):
    if request.method == "POST":
            name = request.POST.get('name')
            desc = request.POST.get('desc')
            release_date = request.POST.get('release_date')
            actors = request.POST.get('actors')
            trailer = request.POST.get('trailer')
            category = request.POST.get('cate')
            poster = request.FILES['poster']
            cate=Category.objects.get(name=category)
            movie=Movies(name=name, desc=desc, trailer=trailer, poster=poster,
                         release_date=release_date,actors=actors,category=cate)
            movie.save()
            return redirect('/')
    return render(request,'add.html')

def update(request,id):
    movie = Movies.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=Movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')

