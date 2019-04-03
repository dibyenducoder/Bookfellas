from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30)
    #genre = models.ManyToManyField(Genre)
    desc = models.TextField(max_length=200)
    ratings =models.IntegerField()
    
    def __str__(self):
        return self.name