from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ('name',)
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    list_per_page = 20
    ordering = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'old_price','available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created']
    # sets up slug to be generated from product name
    prepopulated_fields = {'slug': ('name',)}