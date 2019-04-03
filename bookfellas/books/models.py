from django.db import models
from author.models import Author
from genres.models import Genre
from users.models import User

class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    isbn = models.CharField(max_length=13)
    desc = models.TextField(max_length=200)
    author = models.ManyToManyField(Author)
    genre = models.ManyToManyField(Genre)
    ratings = models.DecimalField(max_digits=3, decimal_places=2)
    pages = models.IntegerField()
    publish_date = models.DateField()
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField()
    text = models.TextField(max_length=500)
    likes = models.IntegerField()
    
class Comment(models.Model):
    Review =models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField()
    text = models.TextField(max_length=500)
    likes = models.IntegerField()