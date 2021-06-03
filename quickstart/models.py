from django.db import models
from django.db.models.base import Model

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)
    imgpath = models.ImageField(blank=True, null=True)


class Branch(models.Model):
    latitude = models.CharField(max_length=250)
    longitude = models.CharField(max_length=250)
    address = models.CharField(max_length=250)


class Contact(models.Model):
    contacts_choises = [
        (1, "PHONE"),
        (2, "FACEBOOK"),
        (3, "EMAIL")
    ]
    contacts = models.IntegerField(choices=contacts_choises, default=1)
    value = models.CharField(max_length=300)


class Course(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=1000)
    category = models.ForeignKey(
        'Category', related_name='categories', on_delete=models.CASCADE)
    logo = models.ImageField(blank=True, null=True)
    contacts = models.ForeignKey(
        'Contact', related_name='contactes', on_delete=models.CASCADE)
    branches = models.ForeignKey(
        'Branch', related_name='branches', on_delete=models.CASCADE)
