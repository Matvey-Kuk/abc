from django.db import models


class Lead(models.Model):
    deviceId = models.CharField(max_length=900, default='')
    mail = models.CharField(max_length=100, default='')


class Message(models.Model):
    lead = models.ForeignKey(Lead)
    from_admin = models.BooleanField(default=False)
    deviceId = models.CharField(max_length=900, default='')
    mail = models.CharField(max_length=100, default='')