from django.urls import path
from .views import *
urlpatterns=[
    path("",index,name='main-page'),
    path("top-sellers/",sellers,name='sellers'),
    path("login/",login,name='login'),
    path("register/",register,name='register'),
    path('profile/',profile,name='profile'),
    path("advertisement/",advertisement,name='advertisement'),
    path('advertisement-post/',post,name='post')
]