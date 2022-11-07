from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import product_all


class TestViewsResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        Category.objects.create(name="django", slug="django")
        User.objects.create(username="user")
        self.data1 = Product.objects.create(
            category_id=1,
            title="django",
            created_by_id=1,
            slug="django-book",
            price="20.00",
            image="default"
        )

    def test_url_allowed_hosts(self):
        """Test allowed hosts.
        """
        response = self.c.get("/", HTTP_HOST="anotherhost.com")
        self.assertEqual(response.status_code, 400)
        response = self.c.get("/", HTTP_HOST="mydomain.com")
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """Test Product response status.
        """
        response = self.c.get(
            reverse("store:product_detail", args=["django-book"])
        )
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """Test Category response status.
        """
        response = self.c.get(
            reverse("store:category_list", args=["django"])
        )
        self.assertEqual(response.status_code, 200)

    def test_homepage_url(self):
        """Test homepage response status.
        """
        request = HttpRequest()
        response = product_all(request)
        html = response.content.decode("utf8")
        self.assertIn("<title>BookStore</title>", html)
        self.assertTrue(html.startswith("\n<!DOCTYPE html>\n"))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        request = self.factory.get("/item/django-book")
        response = product_all(request)
        html = response.content.decode("utf8")
        self.assertIn("<title>BookStore</title>", html)
        self.assertTrue(html.startswith("\n<!DOCTYPE html>\n"))
        self.assertEqual(response.status_code, 200)
