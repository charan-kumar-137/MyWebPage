from django.db import models

# Create your models here.

class Registration(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    phone = models.IntegerField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=15)
    zip = models.IntegerField()
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name