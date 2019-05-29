from django.db import models

# Create your models here.


class ContactUs(models.Model):
      Name = models.CharField(max_length=100)
      Email = models.EmailField()
      subject = models.CharField(max_length=100)
      Message = models.CharField(max_length=200)


def __str__(self):
    return self.Name


class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone = models.CharField(max_length=100)
    Message = models.CharField(max_length=200)


def __str__(self):
    return self.Name