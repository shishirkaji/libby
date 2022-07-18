import django_filters
from .models import Author, Book


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author__first_name = django_filters.CharFilter(lookup_expr='icontains')
    author__last_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ('title', 'author__first_name', 'author__last_name')


class AuthorFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Author
        fields = ('first_name', 'last_name')
