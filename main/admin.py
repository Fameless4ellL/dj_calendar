from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from main import models
from main.models import User, Event


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'link', 'date', 'created', 'updated']
    list_display_links = ['id', 'user']
    search_fields = ['user__username']