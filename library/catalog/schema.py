from graphene import Interface, relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .api.serializers import BookSerializer, AuthorSerializer
from graphene_django.rest_framework.mutation import SerializerMutation
from .filters import AuthorFilter, BookFilter
from .models import Book, Author

# 1. Each django object becomes a "node" in GraphQL


class BookNode(DjangoObjectType):
    class Meta:
        model = Book
        filter_field = []
        interface = (relay.Node, )


class AuthorNode(DjangoObjectType):
    class Meta:
        model = Author
        filter_field = []
        interface = (relay.Node, )


# Problem : If we update a book, that belongs to an Author,
# we will run into an issue with Django REST Framework
# (Nested Serializer)
class BookMutation(SerializerMutation):
    class Meta:
        serializer_class = BookSerializer


class Query(ObjectType):
    book = relay.Node.Field(BookNode)
    books = DjangoFilterConnectionField(BookNode, filterset_class=BookFilter)
    author = relay.Node.Field(AuthorNode)
    authors = DjangoFilterConnectionField(
        AuthorNode, filterset_class=AuthorFilter)


class Mutation(ObjectType):
    book_mutation = BookMutation.Field()
