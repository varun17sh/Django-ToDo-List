from datetime import date
from django.db import models
from django.forms import BooleanField, CharField, DateTimeField

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    creationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title