from django.urls import path
from . import views

app_name='reviewapp'
urlpatterns=[
    path('', views.review_page, name='review_page'),
]