import datetime

from django.db import models
from django.utils import timezone
import sqlite3

#from polls.models import Poll, Snacks
#from django.utils import timezone
#In [1]: p.snacks_set.create(name="test snack1",source_ID=1234,optional="maybe",purchaseLocation="test location",purchaseCount=1,lastPurchaseDate=timezone.now(),votes=0)

class Poll(models.Model):
    category = models.CharField(max_length=255)
    pub_date = models.DateField()
    #p = Poll(category="current", pub_date=timezone.now())

class Snacks(models.Model):
    name = models.CharField(max_length=255)
    source_ID = models.CharField(max_length=6) #formally snack_ID
    optional = models.CharField(max_length=6)
    purchaseLocation = models.CharField(max_length=255)
    purchaseCount = models.IntegerField(default=0)
    lastPurchaseDate = models.DateField()
    votes = models.IntegerField(default=0)
    poll = models.ForeignKey(Poll) #formally formerCurrent
    #s = Snacks(name="test snack1",source_ID=1234,optional="maybe",purchaseLocation="test location",purchaseCount=1,lastPurchaseDate=timezone.now(),votes=0)

class voters(models.Model):
    cookieData = models.CharField(max_length=255)
    timesVoted = models.IntegerField(default=0)

# class Poll(models.Model):
#     category = models.CharField(max_length=255)
#     pub_date = models.DateField()
#
# class snacks(models.Model):
#     name = models.CharField(max_length=255)
#     snack_ID = models.CharField(max_length=6)
#     optional = models.CharField(max_length=6)
#     purchaseLocation = models.CharField(max_length=255)
#     purchaseCount = models.IntegerField(default=0)
#     lastPurchaseDate = models.DateField()
#     votes = models.IntegerField(default=0)
#     formerCurrent = models.ForeignKey(Poll)


    # def __unicode__(self):  # Python 3: def __str__(self):
    #     return self.name





                    #     ID VARCHAR(5),
                    # Name VARCHAR(255) NOT NULL,
                    # Optional VARCHAR (6) NOT NULL,
                    # PurchaseLocation VARCHAR(255) NOT NULL,
                    # PurchaseCount INT NOT NULL,
                    # LastPurchaseDate VARCHAR(12) NOT NULL
