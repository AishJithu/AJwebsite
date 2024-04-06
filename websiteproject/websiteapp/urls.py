from django.urls import path
from . import views

app_name='websiteapp'
urlpatterns = [
    # path('',views.demo,name='demo'),
    path('addmovie/',views.addmovie,name='addmovie'),
    path('allMovieCat/',views.allmovieCat,name='allMovieCat'),
    path('<slug:c_slug>/',views.allmovieCat,name='movies_by_category'),
    path('<slug:c_slug>/<slug:movie_slug>',views.MovieDetail,name='MovieCatDetail'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),



]