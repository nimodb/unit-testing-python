from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Book
from .forms import BookForm


def index(request):
    books = Book.objects.all()
    return render(request, "catalog/index.html", {"books": books})


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("catalog:index"))
    else:
        form = BookForm()
    return render(request, "catalog/add_book.html", {"form": form})
