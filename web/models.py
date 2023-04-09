from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    catagory = models.CharField(max_length=100)

class Report(models.Model):
    name_us = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc_us = models.TextField()
    date = models.DateField()  
    def __str__(self):
        return self.name