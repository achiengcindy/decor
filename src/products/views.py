from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator
from stats import stats
from django.conf import settings
from cart.forms import CartAddProductForm 


def product_list(request):
    page_title = 'Decor Products'
    search_recs = stats.recommended_from_search(request)
    #default object manager
    #products = Product.objects.filter(is_active=True)
    #customized actve manager
    products = Product.active.all()
    bestseller = Product.objects.filter(is_bestseller=True)
    featured = Product.featured.all()[0:settings.PRODUCTS_PER_ROW]
    recently_viewed = stats.get_recently_viewed(request)
    view_recs = stats.recommended_from_views(request)
    return render(request,'product/list.html',{ 'products': products, 'bestseller':bestseller,'featured':featured,'search_recs':search_recs})


def list_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.product_set.all()
    page_title = category.name
    # meta_keywords = category.meta_keywords
    meta_description = category.meta_description
    return render(request, "product/category.html", {'category':category, 'products':products})



def product_detail(request, id, slug):
    p = get_object_or_404(Product, id=id,slug=slug)
    c = p.categories.filter(is_active=True)
    cart_product_form = CartAddProductForm()
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    stats.log_product_view(request, p)
    return render(request, "product/detail.html", {'c':c, 'p':p, 'cart_product_form': cart_product_form,})


    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    categories = product.categories.filter(is_active=True)
   




