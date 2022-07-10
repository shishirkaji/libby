from django.db import models


class Book(models.Model):

    title = models.CharField(max_length=200)
    summary = models.TextField(
        max_length=1000, help_text='Enter a brief description')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    class Meta:

        ordering = ['title']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title


class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self) -> str:
        return f'{self.last_name}, {self.first_name}'
