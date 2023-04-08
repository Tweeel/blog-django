from django.db import models
from datetime import datetime
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    category = models.CharField(max_length=200, default='uncategorized')

    def __str__(self):
        return self.title
