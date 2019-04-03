from django.db import models
from books.models import Book

class User(models.Model):
    username = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_id = models.EmailField(default='abc12345@gmail.com')
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, default='M', choices=(('M','Male'),('F','Female'),('O','Others')))
    bio = models.TextField(max_length=100, blank=True)
    books = models.ManyToManyField(Book, through='Read_status')
    
    def __str__(self):
        return self.username
    
class Read_status(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    READ_CHOICES=(('R','Read'),('IR','Is reading'),('WR','Wants to read'))
    read_status = models.CharField(max_length=20, choices =READ_CHOICES)
    date_added = models.DateField()