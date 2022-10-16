from django.contrib.auth.models import AbstractUser, Group
from django.db import models


# Create your models here.
class User(AbstractUser):
    pass


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    group = models.ManyToManyField(Group)
    headline = models.CharField(max_length=255)
    link = models.URLField()
    date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
