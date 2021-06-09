

# Create your models here.
from django.db import models


# Create your models here.

class tbl_Login(models.Model):

    email = models.CharField(max_length=50, default='')
    password = models.CharField(max_length=50, default='')


    def __str__(self):
        return self.email

    empAuth_objects = models.Manager()