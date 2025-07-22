from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article, Product, Review, UserProfile, VisitHistory, ContactMessage, Upload, Category, Event
from .forms import RegisterForm, ProductForm, ReviewForm, UserProfileForm,ContactMessageForm, UploadForm, CategoryForm, ArticleForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse


# Home page — show articles and products
def home(request):
    articles = Article.objects.all()
    products = Product.objects.all()

    # User history tracking
    visit_count = request.session.get('visit_count', 0)
    request.session['visit_count'] = visit_count + 1
    cart = request.session.get('cart', {})
    return render(request, 'main/home.html', {
        'articles': articles,
        'products': products,
        'visit_count': visit_count,
        'cart': cart,
    })


# Article listing (Class-based)
class ArticleListView(ListView):
    model = Article
    template_name = 'main/articles.html'
    context_object_name = 'articles'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(title__icontains=q)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context


# Article detail (Class-based)
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'main/article_detail.html'
    context_object_name = 'article'


# Product listing
def product_list(request):
    q = request.GET.get('q', '')
    products = Product.objects.all()
    if q:
        products = products.filter(name__icontains=q)
    cart = request.session.get('cart', {})
    return render(request, 'main/products.html', {'products': products, 'cart': cart, 'q': q})


# Product detail view
class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'
    context_object_name = 'product'

# Product create view
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'
    success_url = reverse_lazy('products')

# Product update view
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'
    success_url = reverse_lazy('products')

# Product delete view
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'main/product_confirm_delete.html'
    success_url = reverse_lazy('products')

# Review create view
class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'main/review_form.html'
    success_url = reverse_lazy('products')

# Submit idea (placeholder for future upload/submit feature)
@login_required
def submit_idea(request):
    # To be implemented with new models/forms
    messages.info(request, 'This feature will be updated soon!')
    return redirect('dashboard')

# UserProfile view and update
@login_required
def profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'main/profile.html', {'form': form})

# # TeamMember list and detail
# class TeamMemberListView(ListView):
#     model = TeamMember
#     template_name = 'main/team.html'
#     context_object_name = 'team_members'

# class TeamMemberDetailView(DetailView):
#     model = TeamMember
#     template_name = 'main/team_member_detail.html'
#     context_object_name = 'member'

# ContactMessage create view
class ContactMessageCreateView(CreateView):
    model = ContactMessage
    form_class = ContactMessageForm
    template_name = 'main/contact_form.html'
    success_url = reverse_lazy('home')

# # Event list and detail
class EventListView(ListView):
    model = Event
    template_name = 'main/events.html'
    context_object_name = 'events'

# class EventDetailView(DetailView):
#     model = Event
#     template_name = 'main/event_detail.html'
#     context_object_name = 'event'

# class EventCreateView(LoginRequiredMixin, CreateView):
#     model = Event
#     form_class = EventForm
#     template_name = 'main/event_form.html'
#     success_url = reverse_lazy('events')

# Upload create and list
class UploadCreateView(LoginRequiredMixin, CreateView):
    model = Upload
    form_class = UploadForm
    template_name = 'main/upload_form.html'
    success_url = reverse_lazy('dashboard')

class UploadListView(LoginRequiredMixin, ListView):
    model = Upload
    template_name = 'main/uploads.html'
    context_object_name = 'uploads'
    def get_queryset(self):
        return Upload.objects.filter(user=self.request.user)

# Category list and detail
class CategoryListView(ListView):
    model = Category
    template_name = 'main/categories.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'main/category_detail.html'
    context_object_name = 'category'

# Update dashboard to show user uploads, reviews, and visit history
@login_required
def dashboard(request):
    uploads = Upload.objects.filter(user=request.user)
    reviews = Review.objects.filter(user=request.user)
    visit_count = request.session.get('visit_count', 0)
    visit_history = VisitHistory.objects.filter(user=request.user)
    return render(request, 'main/dashboard.html', {
        'uploads': uploads,
        'reviews': reviews,
        'visit_count': visit_count,
        'visit_history': visit_history,
    })

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

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def add_to_cart(request, product_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        cart[str(product_id)] = cart.get(str(product_id), 0) + 1
        request.session['cart'] = cart
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return HttpResponse(status=200)
    return redirect('home')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return HttpResponse(status=200)
    return redirect('cart')


def cart_view(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        products.append({'product': product, 'quantity': quantity, 'subtotal': product.price * quantity if product.price else 0})
        total += product.price * quantity if product.price else 0
    return render(request, 'main/cart.html', {'cart_items': products, 'total': total})

# Article create view
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'main/article_form.html'
    success_url = reverse_lazy('articles')
