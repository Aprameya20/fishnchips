from django.db import models
import hashlib

class a_fleet (models.Model):
    id = models.AutoField(primary_key=True)
    fishName = models.CharField(max_length=100)
    quantity = models.IntegerField()
    type = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    lat = models.FloatField()
    lon = models.FloatField()
    company = models.CharField(max_length=50)

class b_subfleet(models.Model):
    fleetid = models.ForeignKey(a_fleet, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField()


class c_wholesaler(models.Model):
    subfleetid = models.ForeignKey(b_subfleet, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField()

class d_retailer(models.Model):
    wholesalerid = models.ForeignKey(c_wholesaler, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField()

class e_consumer(models.Model):
    retailerid = models.ForeignKey(d_retailer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField()