from django.urls import path
from users_app import views
from django.contrib.auth import views as auth_viewa

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', auth_viewa.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_viewa.LogoutView.as_view(), name='logout'),

]