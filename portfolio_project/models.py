from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# from django.contrib.gis.db import models
from django.db import models
from location_field.models.plain import PlainLocationField
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    home_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    location = PlainLocationField()
