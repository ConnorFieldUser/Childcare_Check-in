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
    profile = models.ForeignKey(User)

    def __str__(self):
        return "{}, {}".format(self.last, self.first)


ACCESS_LEVELS = [
    ('S', 'Staff'),
    ('P', 'Parent'),
]


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    access_level = models.CharField(max_length=1, choices=ACCESS_LEVELS)

    def __str__(self):
        return str(self.user)

    @property
    def owner(self):
        return self.access_level == 'S'

    @property
    def parent(self):
        return self.access_level == 'P'


@receiver(post_save, sender="auth.User")
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance, access_level='P')
