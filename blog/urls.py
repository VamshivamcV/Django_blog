from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import TailwindLoginForm


urlpatterns = [
    path('', views.post_home, name='post_home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('base', views.base, name='base'),
    path('blog', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail,  name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html', authentication_form=TailwindLoginForm),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]