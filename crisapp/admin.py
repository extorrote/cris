from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import NewsletterSubscription

@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')  # Customize columns to display
    search_fields = ('email',)  # Optional: Add search functionality
