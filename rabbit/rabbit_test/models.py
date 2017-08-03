from django.db import models
from django.contrib.auth.models import User


class Rabbit(models.Model):
    name = models.CharField(max_length=20)
    file = models.FileField(upload_to='uploads', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    guid = models.TextField(null=True, blank=True)
    date_upload = models.DateField(auto_now=True)
