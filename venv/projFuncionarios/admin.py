from django.contrib import admin
from projFuncionarios.models import Author, Genre, Book, BookInstance

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)



