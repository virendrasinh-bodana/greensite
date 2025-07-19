from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Category, Article, Product, Review, UserProfile, VisitHistory, ContactMessage,Upload

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'image']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['product', 'rating', 'comment']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']

class VisitHistoryForm(forms.ModelForm):
    class Meta:
        model = VisitHistory
        fields = ['user', 'session_key', 'visit_count']

# class TeamMemberForm(forms.ModelForm):
#     class Meta:
#         model = TeamMember
#         fields = ['name', 'role', 'bio', 'photo']

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

# class EventForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = ['title', 'description', 'date', 'location', 'organizer']

class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['file', 'description']
