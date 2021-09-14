from django.db import models
from django.db.models.base import Model

class Product(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to ="products",default = "no_image.png")
    price = models.FloatField(help_text="in US dollars $")
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.created.strftime("%d/%m/%Y")}'

