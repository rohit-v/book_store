# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as OrigUserAdmin

User = get_user_model()


@admin.register(User)
class UserAdmin(OrigUserAdmin):
    list_display = (
        'id', 'first_name', 'last_name', 'username',
        'email', 'is_active'
    )
