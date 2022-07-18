from rest_framework import serializers
from catalog.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name')


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)

    class Meta:
        model = Book
        fields = '__all__'
        # 1. Add a new keyword args to allow updating an id
        extra_kwards = {
            'id': {'read_only': False, 'required': False}
        }

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author, created = Author.objects.get_or_create(**author_data)
        book = Book.objects.create(author=author, **validated_data)
        return book

    def update(self, instance, validated_data):
        author_data = validated_data.pop('author')
        author, created = Author.objects.get_or_create(**author_data)
        instance.author = author
        for attr, value in validated_data.items():
            setattr(instance, attr,value)
        instance.save()
        return instance