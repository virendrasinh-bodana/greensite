from django.contrib import admin
from .models import Category, Article, Product, Review, UserProfile, VisitHistory, TeamMember, ContactMessage, Event, Upload

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(UserProfile)
admin.site.register(VisitHistory)
admin.site.register(TeamMember)
admin.site.register(ContactMessage)
admin.site.register(Event)
admin.site.register(Upload) 