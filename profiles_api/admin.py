from django.contrib import admin
from profiles_api import models

# Register the new custom models here.
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
