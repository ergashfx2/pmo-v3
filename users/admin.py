from django.contrib import admin
from .models import Profile,Team

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','status']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id','name']
