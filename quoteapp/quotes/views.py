from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Quote, Author, Tag


def index(request, page=1):
    per_page = 10
    paginator = Paginator(Quote.objects.all(), per_page)
    quotes_on_page = paginator.page(page)
    context = {
        'quotes_and_tags': [
        {
            'quote': quote,
            'tags': quote.tags.all(),
            'author_id': quote.author.id    # type: ignore
        }
        for quote in quotes_on_page
        ],
        'quotes': quotes_on_page,
    }
    return render(request, 'quotes/index.html', context)


def tag_details(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    quotes = Quote.objects.filter(tags__in=[tag])
    context = {
        'tag': tag,
        'quotes_and_tags': [
        {
            'quote': quote,
            'tags': quote.tags.all(),
            'author_id': quote.author.id    #type: ignore
        }
        for quote in quotes
        ]
    }
    return render(request, 'quotes/tag_details.html', context)


def author_details(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    context = {'author': author}
    return render(request, 'quotes/author_details.html', context)
