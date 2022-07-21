from django.contrib import admin

from accounts.views import register
from . models import places, user_details
# Register your models here.
admin.site.register(places)
admin.site.register(user_details)