from django.shortcuts import render

from .models import Category, Product


def categories(request):
    """Get all Categories from the "store_categories" table.
    Can access it from each app page.
    """
    return {
        "categories": Category.objects.all()
    }

def all_products(request):
    products = Product.objects.all()
    return render(request, "store/home.html", {"products": products})
