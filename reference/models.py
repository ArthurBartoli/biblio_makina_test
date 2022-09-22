from django.test import TestCase
from django.db import models


class Book(models.Model):
    
    title = models.CharField(max_length=200, verbose_name="Titre")
    og_title = models.CharField(max_length=200, verbose_name="Titre original")
    author = models.CharField(max_length=50, verbose_name="Auteur")
    desc = models.TextField(verbose_name="Description")
    # 14 chars := 13 digits + 4 dash to seperate code and checksum
    isbn = models.CharField(max_length=17, verbose_name="ISBN")
    published_year = models.PositiveIntegerField(verbose_name="Année de publication")
    is_lent = models.BooleanField(default=False, verbose_name="Déjà emprunté ?")


    def __str__(self):
        return self.title