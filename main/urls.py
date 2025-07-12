from django.shortcuts import render
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('products/', views.product_list, name='products'),
    path('submit/', views.submit_idea, name='submit_idea'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('search/', views.search, name='search'),
    path('about/', lambda r: render(r, 'main/about.html'), name='about'),
    path('contact/', lambda r: render(r, 'main/contact.html'), name='contact'),
]
