from django.contrib import admin

from checkin.models import Profile, Day, Child

# Register your models here.

admin.site.register(Child)
admin.site.register(Day)
admin.site.register(Profile)
