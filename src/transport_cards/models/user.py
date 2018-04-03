# encoding: utf-8

from __future__ import unicode_literals

import random

from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Email не может быть пустым')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.raw_password = password
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.raw_password = password
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


@python_2_unicode_compatible
class User(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name='Email',
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Активен',
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name='Администратор',
    )

    def set_random_password(self):
        alphabet = list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
        raw_password = ''.join([random.choice(alphabet) for _ in range(8)])
        super(User, self).set_password(raw_password)
        self.raw_password = raw_password
        return raw_password

    @property
    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
