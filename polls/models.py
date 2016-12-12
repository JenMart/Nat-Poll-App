from django.db import models


class Poll(models.Model):
    category = models.CharField(max_length=255)
    pub_date = models.DateField()


class Snacks(models.Model):
    name = models.CharField(max_length=255)
    source_ID = models.CharField(max_length=6)
    optional = models.CharField(max_length=6)
    purchaseLocation = models.CharField(max_length=255)
    purchaseCount = models.IntegerField(default=0)
    lastPurchaseDate = models.DateField()
    votes = models.IntegerField(default=0)
    poll = models.ForeignKey(Poll)
