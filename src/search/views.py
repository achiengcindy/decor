from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.conf import settings
import json
from django.core import serializers
from products.models import Product
from search import search


def results(request):
    # get current search phrase
    q = request.GET.get('q', '')

    # retrieve the matching products
    matching = search.products(q).get('products', [])
    print(matching)

    # store the search
    search.store(request, q)

    page_title = 'Search Results for: ' + q
    return render(request,"search/results.html", {'q':q})


