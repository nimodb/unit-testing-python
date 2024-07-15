from django.core.management.base import BaseCommand
from catalog.models import Book
from datetime import datetime


class Command(BaseCommand):
    help = "Generate dummy books with German authors"

    def handle(self, *args, **kwargs):
        books = [
            {
                "title": "Der Vorleser",
                "author": "Bernhard Schlink",
                "published_date": "1995-01-01",
            },
            {
                "title": "Die Verwandlung",
                "author": "Franz Kafka",
                "published_date": "1915-11-01",
            },
            {
                "title": "Im Westen nichts Neues",
                "author": "Erich Maria Remarque",
                "published_date": "1929-01-29",
            },
            {
                "title": "Faust",
                "author": "Johann Wolfgang von Goethe",
                "published_date": "1808-01-01",
            },
            {
                "title": "Der Zauberberg",
                "author": "Thomas Mann",
                "published_date": "1924-11-01",
            },
        ]

        for book in books:
            Book.objects.create(
                title=book["title"],
                author=book["author"],
                published_date=datetime.strptime(
                    book["published_date"], "%Y-%m-%d"
                ).date(),
            )

        self.stdout.write(self.style.SUCCESS("Successfully added dummy books"))
