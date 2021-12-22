import datetime
from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.CharField(max_length=255)
    post_date = models.DateTimeField('date posted')

    def __str__(self):
        return self.name

    
