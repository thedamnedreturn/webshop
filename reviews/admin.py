from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'rating', 'created']
    list_filter = ['rating', 'created']
    search_fields = ['user__username', 'product__name', 'text']