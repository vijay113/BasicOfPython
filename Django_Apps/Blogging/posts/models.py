from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=100000)
    created_at = models.DateTimeField(default=datetime.now,blank=True)



