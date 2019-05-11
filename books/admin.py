from django.contrib import admin
from .models import Genre, Author, Book, User, Read_status

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(User)
admin.site.register(Read_status)

