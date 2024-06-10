from django.contrib import admin
from django.urls import path
from .views import*


urlpatterns = [

    path('register/', register, name='register'),
    path('user_delete/<int:user_id>/', user_delete, name='user_delete'),
    path('login/', login_form, name='login_form'),
    path('change-password/<int:user_id>/', change_password, name='change_password'),
    path('profile/<int:user_id>/',profile_page,name='profile'),
    path('profile_update/<int:user_id>/',profile_update,name='profile_update'),
    path('logout/',logout_page,name='logout'),
    path('api/search-users/', search_users, name='search_users'),
    path('home/',home, name='home'),
]
