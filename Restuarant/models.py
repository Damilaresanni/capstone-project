from django.db import models


class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=225, db_index=True)
    no_of_guests = models.IntegerField()
    bookingDate = models.DateTimeField(db_index=True)
    
    

class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255 ,db_index=True)
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    inventory = models.IntegerField()
    
    