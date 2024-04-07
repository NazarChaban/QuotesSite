from django.core.management.base import BaseCommand
from quotes.models import Author, Quote, Tag
import json

class Command(BaseCommand):
    help = 'Load data into the database'

    def handle(self, *args, **options):
        self.load_authors_to_postgres()
        self.load_tags_to_postgres()
        self.load_quotes_to_postgres()

    def load_authors_to_postgres(self):
        with open('utils/authors.json', 'r') as file:
            authors_data = json.load(file)
            for author_data in authors_data:
                Author.objects.create(
                    fullname=author_data['fullname'],
                    born_date=author_data['born_date'],
                    born_location=author_data['born_location'],
                    description=author_data['description']
                )

    def load_tags_to_postgres(self):
        with open('utils/tags.json', 'r') as file:
            tags_data = json.load(file)
            for tag_data in tags_data:
                Tag.objects.create(
                    name=tag_data['name']
                )

    def load_quotes_to_postgres(self):
        with open('utils/quotes.json', 'r') as file:
            quotes_data = json.load(file)
            for quote_data in quotes_data:
                author = Author.objects.get(fullname=quote_data['author'])
                quote = Quote.objects.create(
                    author=author,
                    quote=quote_data['quote']
                )
                tags = Tag.objects.filter(name__in=quote_data['tags']).all()
                quote.tags.set(tags)
