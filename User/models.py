from django.db import models
# from Bill import models
# Create your models here.

class user(models.Model):
    id = models.AutoField(primary_key=True, editable=False , unique=True)
    Name = models.CharField(max_length=200)
    Phone_No = models.CharField(max_length=10 , unique=True)
    Email = models.EmailField(max_length=254 , unique= True)
    Check_in = models.DateField(null=True)
    Check_out =models.DateField(null=True)
    # BookingId = models.AutoField(editable=True , null= True)
    RoomNo = models.IntegerField( null= True, unique=True)

    def __str__(self):
        return self.Name


