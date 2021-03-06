from django.db import models
import uuid
import random
#from datetime import datetime

#now = datetime.now()
import hashlib

class a_fleet (models.Model):
    id = models.AutoField(primary_key=True)
    fishName = models.CharField(max_length=100)
    quantity = models.IntegerField()
    type = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    #word = now.strftime("%m/%d/%Y, %H:%M:%S")
    lat = models.FloatField()
    lon = models.FloatField()
    company = models.CharField(max_length=50)
    #print(id)
    #blockchain_addr = models.CharField(max_length=64,default=hashlib.sha256(str(id).encode('utf-8')).hexdigest())
    blockchain_address = models.UUIDField(default=uuid.uuid4)


class b_subfleet(models.Model):
    fleetid = models.ForeignKey(a_fleet, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField()
    blockchain_address = models.UUIDField(default=uuid.uuid4)


class c_wholesaler(models.Model):
    subfleetid = models.ForeignKey(b_subfleet, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField()
    blockchain_address = models.UUIDField(default=uuid.uuid4)

class d_retailer(models.Model):
    wholesalerid = models.ForeignKey(c_wholesaler, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField()
    blockchain_address = models.UUIDField(default=uuid.uuid4)

class e_consumer(models.Model):
    retailerid = models.ForeignKey(d_retailer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField()
    blockchain_address = models.UUIDField(default=uuid.uuid4)