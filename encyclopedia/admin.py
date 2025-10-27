from django.contrib import admin
from .models import Category, Entry


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by', 'created_at', 'updated_at']
    search_fields = ['title', 'content']
    list_filter = ['categories', 'created_at', 'updated_at']
    filter_horizontal = ['categories']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('created_by').prefetch_related('categories')