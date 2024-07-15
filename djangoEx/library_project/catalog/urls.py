from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_book, name="add_book"),
]
