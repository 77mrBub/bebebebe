from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
