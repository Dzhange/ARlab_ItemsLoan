
from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

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

STATUS_LIST = {
        ('PF','Perfect'),
        ('SB','Slightly Broken'),
        ('TB','Toltally Broken'),
    }

class Stuff(models.Model):
    spec = models.CharField(max_length = 2,choices = STUFF_NAME)
    status = models.CharField(max_length = 2, choices = STATUS_LIST)
    device_id = models.IntegerField(unique=True)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.spec + ' ' + str(self.device_id)
    
class Room(models.Model):
    spec = models.CharField(max_length = 2,choices = ROOM_LIST)
    is_booked = models.BooleanField(default = False)
    
    def __str__(self):
        return self.spec

class BorrowRecord(models.Model):
    StartTime = models.DateTimeField()
    EndTime =  models.DateTimeField()
    ApplyTime = models.DateTimeField()
    is_approved = models.BooleanField(default=False)
    StuffToUse = models.ManyToManyField(Stuff,blank = True)
    RoomToUse = models.ManyToManyField(Room,blank = True)
    borrower= models.ForeignKey(User, on_delete=models.CASCADE)

    
    