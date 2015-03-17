from django.db import models


class Lead(models.Model):
    is_admin = models.BooleanField(default=False)
    deviceId = models.CharField(max_length=900, default='')
    mail = models.CharField(max_length=100, default='', blank=True)


class Message(models.Model):
    from_lead = models.ForeignKey(Lead, related_name='message_from_lead')
    to_lead = models.ForeignKey(Lead, related_name='message_to_lead')
    has_been_read_by_receiver = models.BooleanField(default=False)
    body = models.CharField(max_length=10000, default='')