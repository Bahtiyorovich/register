from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(blank=True, null=True, max_length=20)
    company = models.CharField(blank=True, null=True, max_length=255)
    subject = models.CharField(blank=True, null=True, max_length=255)
    exist = models.CharField(max_length=3)

    def __str__(self):
        return self.first_name + " " + self.last_name