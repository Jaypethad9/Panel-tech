from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home,name="home"),
    path("login",views.login,name='login'),
    path("logout",views.logout,name='logout'),
    path("register",views.register,name='register'),
    path("about",views.about,name='about'),
    path("search",views.search,name='search'),
    path("contact",views.contact,name='contact'),
]
