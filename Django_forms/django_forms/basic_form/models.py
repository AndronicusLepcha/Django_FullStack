from django.db import models

# Create your models here.
class UserData(models.Model):
    firstname = models.CharField(max_length=100)
    email = models.EmailField()

