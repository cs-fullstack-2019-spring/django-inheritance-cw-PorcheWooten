from django.db import models

# Create your models here.

class contactModel(models.Model):
    email = models.EmailField(default="")
    name = models.CharField(max_length=200, default="")
    subject = models.CharField(max_length=200, default="")
    message = models.TextField(max_length=2000)