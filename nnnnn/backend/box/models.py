from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=100, null=False)
    username = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.email