from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request):
    page_title = 'Decor Products'
    products = Product.active.all()
    bestseller = Product.objects.filter(is_bestseller=True)
    # featured = Product.featured.all()
    return render(request,'product/list.html',{ 'products': products, 'featured':featured, 'bestseller':bestseller})


def list_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.product_set.all()
    page_title = category.name
    meta_keywords = category.meta_keywords
    meta_description = category.meta_description
    return render(request, "product/category.html", {'category':category, 'products':products})



def product_detail(request, slug):
    p = get_object_or_404(Product, slug=slug)
    c = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    return render(request, "product/detail.html", {'c':c, 'p':p})



