from django.shortcuts import render
import os
import json

MODULE_DIR = os.path.dirname(__file__)


def index(request):
    context = {"title": "GeekShop - главная"}
    return render(request, 'products/index.html', context)


def products(request):
    context = {"title": "GeekShop - каталог"}
    file_path = os.path.join(MODULE_DIR, "fixtures/goods.json")
    file_path2 = os.path.join(MODULE_DIR, "fixtures/categories.json")
    context["products"] = json.load(open(file_path, encoding='UTF-8'))
    context["categories"] = json.load(open(file_path2, encoding='UTF-8'))
    return render(request, 'products/products.html', context)
