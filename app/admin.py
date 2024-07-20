from django.contrib import admin

# Register your models here.
from .models import *

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('name','location')
admin.site.register(User)