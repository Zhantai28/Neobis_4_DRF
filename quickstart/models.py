from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)
    imgpath = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=1000)
    category = models.ForeignKey(
        'Category', related_name='categories', on_delete=models.CASCADE)
    logo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    latitude = models.CharField(max_length=250)
    longitude = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    course = models.ForeignKey(
        Course, related_name='branches', on_delete=models.CASCADE)

    def __str__(self):
        return self.address


class Contact(models.Model):
    contacts_choises = [
        (1, "PHONE"),
        (2, "FACEBOOK"),
        (3, "EMAIL")
    ]
    type = models.IntegerField(choices=contacts_choises, default=1)
    value = models.CharField(max_length=300)
    course = models.ForeignKey(
        Course, related_name='contacts', on_delete=models.CASCADE)

    def __str__(self):
        return self.value
