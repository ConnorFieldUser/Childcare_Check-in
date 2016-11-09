from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save

from django.contrib.auth.models import User


# Create your models here.


class Child(models.Model):

    first = models.CharField(max_length=10)
    last = models.CharField(max_length=10)
    pin = models.IntegerField(unique=True)
    profile = models.ForeignKey(User)

    @property
    def active_day(self):
        return self.day_set.get(active=True)

    def __str__(self):
        return "{}, {}".format(self.last, self.first)


ACCESS_LEVELS = [
    ('S', 'Staff'),
    ('P', 'Parent'),
]


class Day(models.Model):

    checkin = models.DateTimeField(auto_now_add=True)
    checkout = models.DateTimeField(auto_now=True, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    hours = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
    child = models.ForeignKey(Child)

    def __str__(self):
        return "{}/{}".format(self.checkin, self.checkout)


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    access_level = models.CharField(max_length=1, choices=ACCESS_LEVELS)

    def __str__(self):
        return str(self.user)

    @property
    def is_staff(self):
        return self.access_level == 'S'

    @property
    def is_parent(self):
        return self.access_level == 'P'


@receiver(post_save, sender="auth.User")
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance, access_level='P')
