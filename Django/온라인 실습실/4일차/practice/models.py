from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.TextField()
    pubdate = models.DateField(auto_now=True)
    price = models.IntegerField()
    adult = models.BooleanField()
