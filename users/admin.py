from django.contrib import admin
from .models import Profile, Order, User_info

admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(User_info)