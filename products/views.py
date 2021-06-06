from django.shortcuts import render
import os
import json
from products.models import ProductCategory, Product

MODULE_DIR = os.path.dirname(__file__)


def index(request):
    context = {"title": "GeekShop - главная"}
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
