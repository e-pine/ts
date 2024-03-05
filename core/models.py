from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Office(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, unique=True)
    def __str__(self):
        return self.name
    
class EquipmentType(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, unique=True)
    def __str__(self):
        return self.name

class Hopps(models.Model):
    office = models.ForeignKey(Office, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True, unique=True)
    last_name = models.CharField(max_length=50, blank=True, null=True, unique=True)
    equip_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=50, blank=True, null=True, unique=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    staff = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='hopps')

    def __str__(self):
         return f"{self.office}"