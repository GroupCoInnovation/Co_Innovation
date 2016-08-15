#-*- coding:utf-8 -*-
from django.contrib import admin
from User.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'password', 'email', 'root', 'major')
    fieldsets = [
        (None, {'fields':['user_name', 'password', 'major', 'email']}),
        ('root', {'fields':['root'], 'classes':['collapse']}),
    ]
    list_filter = ['root', 'major',]
    search_fields = ['root', 'user_name']

admin.site.register(User, UserAdmin)
