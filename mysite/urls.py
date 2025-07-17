from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('',views.HomePage,name="home"),
     path('output/',views.output,name="output"),

    path('signup/',views.SignUpPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('home/',views.HomePage, name='home'),
    path('logout/',views.logoutPage, name='logout'),
    path('profile/',views.profilepage, name='profile'),
    path('contact/',views.contact, name='contact'),
    path('output/',views.output,name='output'),
    

    path('settings/', views.settings_view, name='settings'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('change-password/', views.CustomPasswordChangeView.as_view(), name='change_password'),

    
]
