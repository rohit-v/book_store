# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class CustomUserBackend(ModelBackend):
    """
    Custom backend for authentication to ensure case insensitive comparison of email
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()
        user = None
        if username is None:
            username = kwargs.get(user_model.USERNAME_FIELD)

        try:
            case_insensitive_user_name_field = f"{user_model.USERNAME_FIELD}__iexact"
            user = user_model._default_manager.get(**{case_insensitive_user_name_field: username})
        except user_model.DoesNotExist:
            pass

        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
