from django.test import TestCase
from django.contrib.auth.models import User

from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self) -> None:
        self.data1 = Category.objects.create(name="potato", slug="potato")

    def test_category_model_entry(self):
        """Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_models_name(self):
        """Test Category model default name
        """
        data = self.data1
        self.assertEqual(str(data), "potato")


class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(name="potato", slug="potato")
        User.objects.create(username="user_potato")
        self.data1 = Product.objects.create(
            category_id=1,
            title="potato book",
            created_by_id=1,
            slug="django_book",
            price="20.00",
            image="default"
        )

    def test_product_model_entry(self):
        """Test Product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))

    def test_product_models_title(self):
        """Test Product model default title
        """
        data = self.data1
        self.assertEqual(str(data), "potato book")
