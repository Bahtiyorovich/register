from django.db import models

# Create your models here.

class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.full_name