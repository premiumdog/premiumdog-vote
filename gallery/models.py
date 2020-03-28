from django.db import models

# Create your models here.
class Gallery(models.Model):
    name = models.CharField(max_length=254)
    img = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.name