# encoding: utf-8

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from .base import BaseModel, CATEGORIES


@python_2_unicode_compatible
class Price(models.Model):
    sum = models.DecimalField(
        max_digits=11,
        decimal_places=0,
        blank=False,
        default=0,
        verbose_name='Цена, сссука не подгружается',
    )
    category = models.CharField(
        choices=CATEGORIES.PTS,
        max_length=1,
        blank=False,
        unique=True,
        null=True,
        verbose_name='Категория'
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок',
        help_text='Отсчет начинается с "0"'
    )

    def __str__(self):
        return 'Ценник для категории {}'.format(self.category)

    class Meta:
        # ordering = ['order']
        verbose_name = 'Ценник'
        verbose_name_plural = 'Ценники'


@python_2_unicode_compatible
class Payment(BaseModel):
    sum = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        blank=True,
        null=False,
        default=0,
        verbose_name='Сумма платежа',
    )
    card = models.OneToOneField(
        'transport_cards.TransportCard',
        blank=False,
        null=True,
        related_name='payment',
        verbose_name='Номер платежа',
    )
    done = models.BooleanField(
        blank=True,
        default=False,
        verbose_name='Платеж принят'
    )

    def __str__(self):
        return 'Платеж №{}'.format(self.id)

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
