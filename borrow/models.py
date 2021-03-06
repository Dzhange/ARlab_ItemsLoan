#encode :utf-8

from django.db import models
from django.contrib.auth.models import User
# from multiselectfield import MultiSelectField

# Create your models here.
ROOM_LIST ={
        ('FR','301'),
        ('ST','All Boots(ABCD) in 302'),
        ('SA','Boot A in 302'),
        ('SB','Boot B in 302'),
        ('SC','Boot C in 302'),
        ('SD','Boot D in 302'),
    }

STUFF_NAME = {
        ('MC','iMac'), 
        ('DT','Ddesktop'),
        ('PT','Printer'),
        ('SP','Speaker'),
        ('EP','EarPhone'),
    }


s_STUFF_NAME = {
        'iMac', 
        'Ddesktop',
        'Printer',
        'Speaker',
        'EarPhone',
    }

s_ROOM_NAME ={
        '301',
        'All Boots(ABCD) in 302',
        'Boot A in 302',
        'Boot B in 302',
        'Boot C in 302',
        'Boot D in 302',
    }


STATUS_LIST = {
        ('PF','Perfect'),
        ('SB','Slightly Broken'),
        ('TB','Toltally Broken'),
    }

s_STATUS_NAME = {
        'Perfect',
        'Slightly Broken',
        'TB','Toltally Broken',
    }
class Stuff(models.Model):
    spec = models.CharField(max_length = 20,choices = STUFF_NAME)
    status = models.CharField(max_length = 2, choices = STATUS_LIST)
    device_id = models.IntegerField(unique=True)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.spec + ':' + str(self.device_id)
    
class Room(models.Model):
    spec = models.CharField(max_length = 2,choices = ROOM_LIST)
    is_booked = models.BooleanField(default = False)
    
    def __str__(self):
        return self.spec
    
class BorrowRecord(models.Model):
    StartTime = models.DateTimeField()
    EndTime =  models.DateTimeField()
    # ApplyTime = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    StuffToUse = models.ManyToManyField(Stuff,blank = True, related_name = 'common')
    OtherRequests = models.CharField(default = '无',max_length=100,blank = True)
    # SecretObjects = models.ManyToManyField(Stuff,blank = True,related_name = 'secret')
    RoomToUse = models.ManyToManyField(Room,blank = True)
    borrower= models.ForeignKey(User, on_delete=models.CASCADE)
    ErrorMessage=models.CharField(default=" ",max_length=500,blank = True)

    
class User(User):

    def __str__(self):
        return self.username