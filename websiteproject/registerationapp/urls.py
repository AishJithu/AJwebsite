from django.urls import path
from . import views
app_name='registerationapp'
urlpatterns = [
    path('',views.demo,name='demo'),
    path('login',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('user',views.user,name='user')

]