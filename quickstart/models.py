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
    email = models.EmailField()
    facebook = models.CharField(max_length=60)
    phone = models.IntegerField(blank=True)


class Course(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=1000)
    category = models.ForeignKey(
        'Category', related_name='categories', on_delete=models.CASCADE)
    logo = models.ImageField(blank=True, null=True)
    contacts = models.ForeignKey(
        'Contact', related_name='contacts', on_delete=models.CASCADE)
    branches = models.ForeignKey(
        'Branch', related_name='branches', on_delete=models.CASCADE)
