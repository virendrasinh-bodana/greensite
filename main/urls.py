from django.shortcuts import render
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('products/', views.product_list, name='products'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/add/', views.ProductCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('review/add/', views.ReviewCreateView.as_view(), name='review_add'),
    path('profile/', views.profile, name='profile'),
    path('team/', views.TeamMemberListView.as_view(), name='team'),
    path('team/<int:pk>/', views.TeamMemberDetailView.as_view(), name='team_member_detail'),
    path('contact/send/', views.ContactMessageCreateView.as_view(), name='contact_send'),
    path('events/', views.EventListView.as_view(), name='events'),
    path('event/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    path('event/add/', views.EventCreateView.as_view(), name='event_add'),
    path('uploads/', views.UploadListView.as_view(), name='uploads'),
    path('upload/add/', views.UploadCreateView.as_view(), name='upload_add'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('submit/', views.submit_idea, name='submit_idea'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('search/', views.search, name='search'),
    path('about/', lambda r: render(r, 'main/about.html'), name='about'),
    path('contact/', lambda r: render(r, 'main/contact.html'), name='contact'),
]
