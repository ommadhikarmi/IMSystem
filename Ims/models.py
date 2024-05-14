from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # This should ideally be a PasswordField
    username = models.CharField(max_length=100, default='username')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class ResourceType(models.Model):  # Renamed class to follow naming convention
    name = models.CharField(max_length=100)

class Department(models.Model):  # Renamed class to follow naming convention
    name = models.CharField(max_length=100)
    floor = models.IntegerField()
    description = models.TextField()

class Resources(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(ResourceType, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    quantity = models.IntegerField()
    departments = models.ManyToManyField(Department)  # Renamed field to plural form

class Vendor(models.Model):  # Renamed class to follow naming convention
    name = models.CharField(max_length=100)
    address = models.TextField()
    company_name = models.CharField(max_length=100)
    contact_no = models.IntegerField()  # Changed field type to CharField

class Purchase(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    resource = models.ForeignKey(Resources, on_delete=models.SET_NULL, null=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField()
