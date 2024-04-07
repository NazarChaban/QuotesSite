from venv import create
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return f'{self.name}'


class Author(models.Model):
    fullname = models.CharField(max_length=150, null=False, unique=True)
    born_date = models.CharField(max_length=150, null=False)
    born_location = models.CharField(max_length=250, null=False)
    description = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'{self.fullname}'


class Quote(models.Model):
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, default=None
    )
    quote = models.TextField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quote}'[:100] + '...' if len(self.quote) > 100 else f'{self.quote}'
