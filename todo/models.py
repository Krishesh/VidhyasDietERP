from django.db import models

# Create your models here.
from django.db import models


class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    trashed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
