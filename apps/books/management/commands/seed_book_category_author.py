from django.core.management import BaseCommand
from apps.books.models import Book, Category, Author


class Command(BaseCommand):
    help = "Seed Category, Author and Book data."

    def handle(self, *args, **kwargs):

    
        # Categories
        
        categories = [
            {"name": "Programming"},
            {"name": "Science Fiction"},
            {"name": "History"},
            {"name": "Business"},
        ]

        created_categories = Category.objects.bulk_create(
            Category(**category) for category in categories
        )

        category_a = created_categories[0]
        category_b = created_categories[1]
        category_c = created_categories[2]
        category_d = created_categories[3]


        # Authors

        authors = [
            {
                "name": "Robert Martin",
                "bio": "Software engineer and author of books about software development.",
            },
            {
                "name": "Isaac Asimov",
                "bio": "American writer and professor known for science fiction.",
            },
            {
                "name": "Yuval Noah Harari",
                "bio": "Historian and author of books about human history.",
            },
            {
                "name": "Peter Drucker",
                "bio": "Management thinker and author.",
            },
        ]

        created_authors = Author.objects.bulk_create(
            Author(**author) for author in authors
        )

        author_a = created_authors[0]
        author_b = created_authors[1]
        author_c = created_authors[2]
        author_d = created_authors[3]

        # Books
        
        books = [
            {
                "name": "Clean Code",
                "category": category_a,
                "author": author_a,
            },
            {
                "name": "The Clean Coder",
                "category": category_a,
                "author": author_a,
            },
            {
                "name": "Foundation",
                "category": category_b,
                "author": author_b,
            },
            {
                "name": "I, Robot",
                "category": category_b,
                "author": author_b,
            },
            {
                "name": "Sapiens",
                "category": category_c,
                "author": author_c,
            },
            {
                "name": "Homo Deus",
                "category": category_c,
                "author": author_c,
            },
            {
                "name": "The Effective Executive",
                "category": category_d,
                "author": author_d,
            },
            {
                "name": "Management: Tasks, Responsibilities, Practices",
                "category": category_d,
                "author": author_d,
            },
        ]

        Book.objects.bulk_create(
            Book(**book) for book in books
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"{len(categories)} categories, "
                f"{len(authors)} authors, "
                f"{len(books)} books seeded successfully."
            )
        )