from django.db import models
from django.utils import timezone


class Lead(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    country = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
