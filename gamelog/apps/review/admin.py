from django.contrib import admin
from user.models import User
# Register your models here.
admin.site.is_registered(User)