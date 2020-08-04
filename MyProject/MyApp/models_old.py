from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Main(models.Model):
    name = models.TextField(default='_')
    f_name = models.TextField(default='_')
    l_name = models.TextField(default='_')
    email = models.TextField(default='_')

   

