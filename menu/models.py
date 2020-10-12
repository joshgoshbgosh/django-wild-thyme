from django.db import models

# Create your models here.
class Menu_Item(models.Model):
    name = models.CharField(max_length=225)
    price = models.CharField(max_length=225)




    def __str__(self):
        return self.name
