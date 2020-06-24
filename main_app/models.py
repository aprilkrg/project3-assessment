from django.db import models

# Create your models here.
class List(models.Model):
    list_text = models.CharField(max_length=1000)

class Item(models.Model):
    item_text = models.CharField(max_length=1000)
