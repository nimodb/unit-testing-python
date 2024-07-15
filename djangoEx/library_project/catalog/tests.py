from django.test import TestCase
from django.urls import reverse
from .models import Book


class BookTests(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book", author="Test Author", published_date="2023-01-01"
        )

    def test_index_view(self):
        response = self.client.get(reverse("catalog:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book.title)

    def test_add_book_view_get(self):
        response = self.client.get(reverse("catalog:add_book"))
        self.assertEqual(response.status_code, 200)

    def test_add_book_view_post(self):
        data = {
            "title": "New Book",
            "author": "New Author",
            "published_date": "2024-01-01",
        }
        response = self.client.post(reverse("catalog:add_book"), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Book.objects.count(), 2)
        self.assertTrue(Book.objects.filter(title="New Book").exists())
