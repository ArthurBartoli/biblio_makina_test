from django.conf import settings
from django.db import models
from django.utils import timezone


class Book(models.Model):

    title = models.CharField(max_length=200)
    og_title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    desc = models.TextField()
    published_year = models.IntegerField()
    # ISBN := 14 chars -> 13-digit + dash separating checksum from code
    # Could be primary key but let's keep it simple
    isbn = models.CharField(max_length=14) 
    is_lent = models.BooleanField()

    def __str__(self):
        return self.title
