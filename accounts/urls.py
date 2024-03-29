from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path, include

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('home/', views.home, name="home"),
    path('signup/',views.signup, name='signup'),
]