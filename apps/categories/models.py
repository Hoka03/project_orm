from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, blank=True)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name