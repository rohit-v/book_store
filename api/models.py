# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


class CustomUser(AbstractUser):
    """
    Model to store user information.
    """
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(
        _('Email Address'),
        unique=True
    )
    password = models.CharField(max_length=100)
    author_pseudonym = models.CharField(
        _('Author Pseudonym'),
        max_length=200,
        default=_('Anonymous')
    )


class Book(models.Model):
    """
    Model to store Book information
    """
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=1000, null=True)
    author =  models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    price = models.IntegerField()
    cover_image = models.URLField(max_length=500)
