from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Article, Product, Idea
from .forms import IdeaForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Home page — show articles and products
def home(request):
    articles = Article.objects.all()
    products = Product.objects.all()

    # User history tracking
    visit_count = request.session.get('visit_count', 0)
    request.session['visit_count'] = visit_count + 1

    return render(request, 'main/home.html', {
        'articles': articles,
        'products': products,
        'visit_count': visit_count,
    })


# Article listing (Class-based)
class ArticleListView(ListView):
    model = Article
    template_name = 'main/article_list.html'
    context_object_name = 'articles'


# Article detail (Class-based)
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'main/article_detail.html'
    context_object_name = 'article'


# Product listing
def product_list(request):
    products = Product.objects.all()
    return render(request, 'main/product_list.html', {'products': products})


# Submit idea
@login_required
def submit_idea(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.user = request.user
            idea.save()
            messages.success(request, 'Your idea has been submitted!')
            return redirect('dashboard')
    else:
        form = IdeaForm()
    return render(request, 'main/submit_idea.html', {'form': form})


# User dashboard
@login_required
def dashboard(request):
    ideas = Idea.objects.filter(user=request.user)
    visit_count = request.session.get('visit_count', 0)
    return render(request, 'main/dashboard.html', {'ideas': ideas, 'visit_count': visit_count})


# Register
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})


# Search
def search(request):
    query = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=query) if query else []
    products = Product.objects.filter(name__icontains=query) if query else []
    return render(request, 'main/search_results.html', {'articles': articles, 'products': products, 'query': query})
