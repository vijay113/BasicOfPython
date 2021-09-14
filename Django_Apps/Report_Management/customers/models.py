from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to="customers",default="no_image.png")


    def __str__(self):
        return str(self.name)

    

