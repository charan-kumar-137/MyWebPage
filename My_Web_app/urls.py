from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    path('handle_signup',views.handle_signup,name='handle_signup'),
    path('handle_login',views.handle_login,name='handle_login'),

]