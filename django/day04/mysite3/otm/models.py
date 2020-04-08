from django.db import models

# Create your models here.
class Publisher(models.Model):

    name = models.CharField(max_length=20,verbose_name='名字')

class Book(models.Model):
    title = models.CharField(max_length=11,verbose_name='书名')

    publisher = models.ForeignKey(Publisher)
