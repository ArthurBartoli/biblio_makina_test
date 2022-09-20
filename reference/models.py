from django.test import TestCase
from django.db import models


class Book(models.Model):
    
    title = models.CharField(max_length=200)
    og_title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    desc = models.TextField()
    # 14 chars := 13 digits + 4 dash to seperate code and checksum
    isbn = models.CharField(max_length=17)
    published_year = models.PositiveIntegerField()
    is_lent = models.BooleanField(default=False)

    def __str__(self):
        return self.title