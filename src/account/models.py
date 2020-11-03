from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import PushID
from django_email_verification import sendConfirm


class Account(AbstractUser):
    email = models.EmailField(verbose_name='email address', unique=True)
    username = models.CharField(verbose_name='account name', max_length=50, unique=False, blank=True)
    user_id = models.CharField(verbose_name='user id', max_length=28, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = PushID().next_id()
        super().save(*args, **kwargs)
