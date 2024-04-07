from mongoengine import connect
from mongo_models import Author as MAuthor, Quote as MQuote
import json

connect(
    db='hw9_db', host='localhost', port=27017,
    username='root', password='example'
)


def load_quotes_to_json():
    quotes = MQuote.objects().all()     # type: ignore
    quotes_list = []
    for quote in quotes:
        quote_dict = {
            'tags': [tag.name for tag in quote.tags],
            'author': quote.author.fullname,
            'quote': quote.quote
        }
        quotes_list.append(quote_dict)

    with open('quotes.json', 'w') as file:
        json.dump(quotes_list, file, indent=4)


def load_authors_to_json():
    authors = MAuthor.objects().all()   # type: ignore
    authors_list = []
    for author in authors:
        author_dict = {
            'fullname': author.fullname,
            'born_date': author.born_date,
            'born_location': author.born_location,
            'description': author.description
        }
        authors_list.append(author_dict)

    with open('authors.json', 'w') as file:
        json.dump(authors_list, file, indent=4)


def load_tags_to_json():
    quotes = MQuote.objects().all()     # type: ignore
    tags_set = set()
    for quote in quotes:
        tags = [tag.name for tag in quote.tags]
        tags_set.update(tags)
    
    tags_list = [{'name': tag} for tag in tags_set]

    with open('tags.json', 'w') as file:
        json.dump(tags_list, file, indent=4)


if __name__ == '__main__':
    load_quotes_to_json()
    load_authors_to_json()
    load_tags_to_json()