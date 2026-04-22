from django.contrib import admin

from Seasons.models import User, Field, Update

# Registered models.

admin.site.register(User)
admin.site.register(Field)
admin.site.register(Update)