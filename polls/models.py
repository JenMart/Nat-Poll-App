import datetime

from django.db import models
from django.utils import timezone
import sqlite3


# class Poll(models.Model):
#     question = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#     def __unicode__(self):  # Python 3: def __str__(self):
#         return self.question
#
#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.pub_date < now
#
#     was_published_recently.admin_order_field = 'pub_date'
#     was_published_recently.boolean = True
#     was_published_recently.short_description = 'Published recently?'
#
#
# class Choice(models.Model):
#     poll = models.ForeignKey(Poll)
#     choice_text = models.CharField(max_length=200) #this!
#     votes = models.IntegerField(default=0)
#
#     def __unicode__(self):  # Python 3: def __str__(self):
#         return self.choice_text
class Poll(models.Model):
    category = models.CharField(max_length=255)
    pub_date = models.DateField()

class snacks(models.Model):
    name = models.CharField(max_length=255)
    snack_ID = models.CharField(max_length=6)
    optional = models.CharField(max_length=6)
    purchaseLocation = models.CharField(max_length=255)
    purchaseCount = models.IntegerField(default=0)
    lastPurchaseDate = models.DateField()
    votes = models.IntegerField(default=0)
    formerCurrent = models.ForeignKey(Poll)


    # def __unicode__(self):  # Python 3: def __str__(self):
    #     return self.name



# class formerSnacks(models.Model):
#     name = models.CharField(max_length=255)
#     optional = models.CharField(max_length=6)
#     purchaseLocation = models.CharField(max_length=255)
#     purchaseCount = models.IntegerField(default=0)
#     lastPurchaseDate = models.DateField()
#     votes = models.IntegerField(default=0)

class voters(models.Model):
    cookieData = models.CharField(max_length=255)
    timesVoted = models.IntegerField(default=0)

                    #     ID VARCHAR(5),
                    # Name VARCHAR(255) NOT NULL,
                    # Optional VARCHAR (6) NOT NULL,
                    # PurchaseLocation VARCHAR(255) NOT NULL,
                    # PurchaseCount INT NOT NULL,
                    # LastPurchaseDate VARCHAR(12) NOT NULL
