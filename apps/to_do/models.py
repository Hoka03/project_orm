from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.validators import MinValueValidator

from apps.categories.models import Category


class ToDo(models.Model):
    user = models.ManyToManyField(User)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1500, blank=True)

    done = models.BooleanField(default=False)
    done_at = models.DateTimeField(blank=True, null=True)

    start_date = models.DateField(default=now)
    days = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title