from django.test import TestCase
from django.db import models


class Book(models.Model):
    
    title = models.CharField(max_length=200)
    og_title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    desc = models.TextField()
    # 14 chars := 13 digits + 1 dash to seperate code and checksum
    isbn = models.CharField(max_length=14)
    published_year = models.IntegerField()

    def __str__(self):
        return self.title