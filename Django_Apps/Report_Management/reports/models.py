from django.db.models.fields import DateTimeField
from profiles.models import Profile
from django.db import models
from django.utils import tree
from profiles.models import Profile

class Report(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="reports",blank=True)
    remarks = models.TextField()
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)




