from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Welfare(models.Model):
    user = models.ForeignKey(User, related_name='user')
    address = models.TextField()
    content = models.CharField(max_length=100) 
    note = models.CharField(max_length=100) 
    urgent = models.CharField(max_length=10) 
    helpType = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    helpUser = models.ForeignKey(User, blank=True, null=True, related_name='helpUser')
    lat = models.FloatField(blank=True, null=True)  #精度
    lng = models.FloatField(blank=True, null=True)  #緯度
    
    def __str__(self):
        return self.user.username + ', ' + self.address