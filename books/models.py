from django.db import models
from django.contrib.auth.models import AbstractUser

class Genre(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField(max_length=150)
    
    def __str__(self):
        return self.name

    def get_books(self):
        return self.book_set.all()

class Author(models.Model):
    name = models.CharField(max_length=30)
    genre = models.ManyToManyField(Genre)
    desc = models.TextField(max_length=200)
    ratings =models.IntegerField()
    
    def __str__(self):
        return self.name

    def get_books(self):
        return self.book_set.all()

class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    desc = models.TextField(max_length=200)
    author = models.ManyToManyField(Author)
    genre = models.ManyToManyField(Genre)
    ratings = models.DecimalField(max_digits=3, decimal_places=2)
    pages = models.IntegerField()
    publish_date = models.DateField()
    
    def __str__(self):
        return self.title

    @property
    def get_authors(self):
        return self.author.all()
'''
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
'''

class Profile(AbstractUser):
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=10, default='M', choices=(('M','Male'),('F','Female'),('O','Others')))
    bio = models.TextField(max_length=100, blank=True)
    #books = models.ManyToManyField(Book, through='Read_status')
    
    def __str__(self):
        return self.username
'''    
class Read_status(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    READ_CHOICES=(('R','Read'),('IR','Is reading'),('WR','Wants to read'))
    read_status = models.CharField(max_length=20, choices =READ_CHOICES)
    date_added = models.DateField()
'''
