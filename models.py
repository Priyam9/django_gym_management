from django.db import models

class bodyflex_memebers(models.Model):
    firstname = models.CharField(max_length=100,null=True)
    lastname = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100,null=True)
    age = models.CharField(max_length=10,null=True)
    Gender = models.CharField(max_length=10,null=True)
    contact = models.CharField(max_length=10,null=True)
    
