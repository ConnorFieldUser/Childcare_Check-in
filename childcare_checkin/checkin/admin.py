from django.contrib import admin

from checkin.models import Profile, Check, Child

# Register your models here.

admin.site.register(Child)
admin.site.register(Check)
admin.site.register(Profile)
