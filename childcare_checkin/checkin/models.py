from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save

from django.contrib.auth.models import User


# Create your models here.


class Check(models.Model):

    checkin = models.DateTimeField(auto_now=True)
    checkout = models.DateTimeField(auto_now=True)
    hours = models.IntegerField(null=True, blank=True)


class Child(models.Model):

    first = models.CharField(max_length=10)
    last = models.CharField(max_length=10)
    pin = models.IntegerField(unique=True)
    parent = models.ForeignKey(User)


ACCESS_LEVELS = [
    ('s', 'Staff'),
    ('p', 'Parent'),
]


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    access_level = models.CharField(max_length=1, choices=ACCESS_LEVELS)

    def __str__(self):
        return self.access_level

    @property
    def owner(self):
        return self.access_level == 's'

    @property
    def parent(self):
        return self.access_level == 'p'


@receiver(post_save, sender="auth.User")
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance)
