from .models import Category


def categories(request):
    """Get all Categories from the "store_categories" table.
    Can access it from each app page.
    """
    return {
        "categories": Category.objects.all()
    }
