from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    """A model that defines a category of the product in the database.
    """
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    """A model with main data of different products.
    Has a foreign key from the 'Category' table to show a type of product
    and from the 'User' table to show who has created the product.
    """
    category = models.ForeignKey(
        Category,
        related_name="product",
        on_delete=models.CASCADE
    )
    created_by = models.ForeignKey(
        User,
        related_name="product_creator",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default="admin")
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "products"
        ordering = ("-created", )

    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])

    def __str__(self):
        return self.title
