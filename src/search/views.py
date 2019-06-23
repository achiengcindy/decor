from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
import json
from django.core import serializers
from products.models import Product
from search import search

PAGE_SIZE = 20

def results(request):
    # get current search phrase
    q = request.GET.get('q', '')
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1

    # retrieve the matching products
    # matching = search.products(q).get('products', [])
    # print(matching)

    # retrieve the matching products
    matching = search.products(q).get('products')
    print(matching)

    # generate the pagintor object
    paginator = Paginator(matching, 12)
    try:
        results = paginator.page(page).object_list
    except (InvalidPage, EmptyPage):
        results = paginator.page(1).object_list

    # store the search
    search.store(request, q)

    page_title = 'Search Results for: ' + q
    return render(request, "search/results.html", {'q': q})


# def results(request):
#     """ template for displaying settings.PRODUCTS_PER_PAGE paginated product results """
#     # get current search phrase
#     q = request.GET.get('q', '')
#     # get current page number. Set to 1 is missing or invalid
#     try:
#         page = int(request.GET.get('page', 1))
#     except ValueError:
#         page = 1

#     matching = search.products(q).get('products', [])
#     # generate the pagintor object
#     paginator = Paginator(matching,
#                           settings.PRODUCTS_PER_PAGE)
#     try:
#         results = paginator.page(page).object_list
#     except (InvalidPage, EmptyPage):
#         results = paginator.page(1).object_list

#     search.store(request, q)

#     page_title = 'Search Results for: ' + q
#     return render_to_response(template_name, locals(), context_instance=RequestContext(request))


# from django.core.paginator import Paginator
# PAGE_SIZE = 20

# def all_babysitters(request):
#     p = request.query_params.get("page", 1)
#     babysitters = Babysitter.objects.all()
#     paginator = Paginator(babysitters, PAGE_SIZE)
#     # page = paginator.page(p) # ~ Django 1.11
#     # The following line was added, see comments below for why
#     page = paginator.get_page(p) # Django 2.0 +
#     nextpage = page.next_page_number() if page.has_next() else None
#     data = BabySitterSerializer([i for i in page.object_list], many=True)
#     pages = {
#         "current": p,
#         "next": nextpage,
#         "total_pages": paginator.num_pages
#         "total_results": paginator.count
#     }
#     return {
#          "page_data": pages
#          "data": data
#     }