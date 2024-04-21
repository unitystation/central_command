from datetime import timedelta

from django.db import models
from django.utils import timezone


class Server(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=50)
    port = models.IntegerField()
    player_count = models.IntegerField()
    image_link = models.URLField()
    ## TODO: ADD VALIDATION FOR APPROVED API KEYS SO THAT STRANGERS DONT SPAM STATIONHUB WITH INVALID SERVERS ##

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def is_expired(self):
        expiration_time = self.updated_at + timedelta(seconds=10)
        return expiration_time < timezone.now()
