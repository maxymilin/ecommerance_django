from django.urls import path

from . import views

app_name = "busket"

urlpatterns = [
    path("", views.basket_summary, name="basket_summary"),
]