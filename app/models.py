from django.db import models

# Create your models here.


class Worker(models.Model):
    name = models.CharField(max_length=30)


class Item(models.Model):
    inv_num = models.IntegerField()
    brand = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    price = models.IntegerField()
    model = models.CharField(max_length=30)


class Warehouse(models.Model):
    name = models.CharField(max_length=30)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)


class Inventory(models.Model):
    stock = models.ForeignKey(Warehouse, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    balance = models.IntegerField()
