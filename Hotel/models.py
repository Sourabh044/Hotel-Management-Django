from django.db import models

# Ask Sir that can we create a Dictionarry here
class hotel(models.Model):
    id = models.AutoField(primary_key=True , editable=False)
    name = models.CharField(max_length=200, null=False)
    img = models.ImageField(upload_to="imagecontainer")
    desc = models.CharField(max_length=100, null=False)
    # updated = models.DateTimeField(auto_now=True)
    # created = models.DateTimeField(auto_now_add=True)
    # Location = models.CharField(max_length=200, null=True)
    # Location_Maps = models.CharField(max_length=246, null=True)
    FeeCancellation = models.BooleanField(default=True)
    Total_Rooms = models.CharField(max_length=300, null=False, default=100)
    Ratings = models.FloatField(max_length=5, blank=True)
    # Rooms = {}
    # NonACRoom = models.BooleanField
    # CoupleRoom = models.BooleanField

    
    def __str__(self):
        return self.name


