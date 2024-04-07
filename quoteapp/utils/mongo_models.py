from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import (
    ReferenceField,
    StringField,
    ListField,
    EmbeddedDocumentField
)


class Tag(EmbeddedDocument):
    name = StringField()


class Author(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quote(Document):
    tags = ListField(EmbeddedDocumentField(Tag))
    author = ReferenceField(Author)
    quote = StringField()
