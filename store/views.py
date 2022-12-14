from django.shortcuts import get_object_or_404, render

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


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, "store/detail.html", {"product": product})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(
        request,
        "store/category.html",
        {"category": category, "products": products}
    )
