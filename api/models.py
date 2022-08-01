from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(unique=True, max_length=128)
    email = models.EmailField()
    password = models.CharField(max_length=256)
    dob = models.CharField(max_length=128)
    createdAt = models.DateTimeField(auto_now=True)
    modifiedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<User {self.name}, {self.email}>'


class Paragraphs(models.Model):
    paragraph = models.CharField(max_length=4096)
