import datetime

from django.db import models


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
