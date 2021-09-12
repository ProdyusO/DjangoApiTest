from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=100, null=True, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250, null=True, blank=True)
    pages = models.IntegerField(default=1, validators=[MaxValueValidator(700),MinValueValidator(1)])
