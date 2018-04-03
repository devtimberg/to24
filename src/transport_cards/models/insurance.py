# encoding: utf-8

from __future__ import unicode_literals
from django.db import models


class Insurance(models.Model):
    logotype = models.ImageField(
        upload_to='insurance',
        verbose_name='Логотип компании'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Название страховой компании'
    )
    url = models.URLField(
        verbose_name='Ссылка на Е-ОСАГО'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страховая компания'
        verbose_name_plural = 'Страховые компании'