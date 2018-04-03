# encoding: utf-8

from __future__ import unicode_literals

from hashlib import md5

from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible

from .base import BaseModel, CATEGORIES
from .payment import Payment, Price


@python_2_unicode_compatible
class TransportCard(BaseModel):
    (CREATED, WAITING_REQUEST, WAITING_RENDER,
     READY, SENDING_ERROR, RENDER_ERROR) = range(6)

    CARD_STATUSES = (
        (CREATED, 'Ожидает оплаты'),
        (WAITING_REQUEST, 'Ожидает создания'),
        (WAITING_RENDER, 'Ожидает рендера'),
        (READY, 'Готова'),
        (SENDING_ERROR, 'Ошибка при регистрации карты'),
        (RENDER_ERROR, 'Ошибка при рендере'),
    )
    FUEL_TYPES = (
        (None, 'Без топлива'),
        ('Petrol', 'Бензин'),
        ('Diesel', 'Дизельное топливо'),
        ('PressureGas', 'Cжатый газ'),
        ('LiquefiedGas', 'Сжиженный газ'),
    )
    BRAKING_TYPES = (
        (None, 'Без тормозной системы'),
        ('Mechanical', 'Механический'),
        ('Hydraulic', 'Гидравлический'),
        ('Pneumatic', 'Пневматический'),
        ('Combined', 'Комбинированный'),
    )
    DOCUMENT_TYPES = (
        ('RegTalon', 'Свидетельство  регистрации транспортного средства'),
        ('PTS', 'Паспорт транспортного средства'),
    )
    VALIDITY_VALUES = (
        (6, '6'),
        (12, '12'),
        (24, '24'),
    )

    user = models.ForeignKey(
        'transport_cards.User',
        blank=False,
        null=True,
        related_name='transport_cards',
        verbose_name='Пользователь'
    )
    phone = models.CharField(
        max_length=25,
        blank=False,
        null=True,
        verbose_name='Телефон'
    )
    status = models.SmallIntegerField(
        choices=CARD_STATUSES,
        blank=True,
        default=0,
        verbose_name='Статус'
    )
    exception = models.TextField(
        blank=True,
        default='',
        verbose_name='Исключение'
    )
    pdf = models.FileField(
        upload_to='pdf/',
        blank=True,
        null=True,
        verbose_name='PDF'
    )

    # Паспортные данные
    FName = models.CharField(
        max_length=100,
        blank=False,
        default='',
        verbose_name='Имя'
    )
    Name = models.CharField(
        max_length=100,
        blank=False,
        default='',
        verbose_name='Фамилия'
    )
    MName = models.CharField(
        max_length=100,
        blank=True,
        default='',
        verbose_name='Отчество'
    )
    Series = models.CharField(
        max_length=100,
        blank=False,
        default='',
        verbose_name='Серия'
    )
    Number = models.PositiveIntegerField(
        blank=False,
        null=True,
        verbose_name='Номер'
    )
    Organization = models.CharField(
        max_length=100,
        blank=False,
        default='',
        verbose_name='Выдан кем'
    )
    Date = models.DateField(
        blank=False,
        null=True,
        verbose_name='Выдан когда'
    )
    Foreign = models.BooleanField(
        blank=True,
        default=False,
        verbose_name='Иностранный гражданин'
    )

    # Информация о ТС
    specials = models.CharField(
        choices=CATEGORIES.SPECIAL,
        max_length=4,
        blank=True,
        null=True,
        verbose_name='Особенность ТС'
    )
    EAISTO_code = models.CharField(
        max_length=21,
        blank=True,
        default='',
        verbose_name='Код ЕАИСТО'
    )

    BodyNumber = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default='',
        verbose_name='Кузов №'
    )
    Note = models.TextField(
        blank=True,
        default='',
        verbose_name='Замечания'
    )
    RegistrationNumber = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        default='',
        verbose_name='Государственный регистрационный знак'
    )
    VehicleCategory = models.CharField(
        choices=CATEGORIES.PTS,
        max_length=1,
        blank=False,
        null=True,
        verbose_name='СРТС или ПТС'
    )
    VehicleCategory2 = models.CharField(
        choices=CATEGORIES.OKP,
        max_length=2,
        blank=False,
        default='B',
        verbose_name='Категория ТС (ОКП)'
    )
    VIN = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default='',
        verbose_name='VIN'
    )
    Year = models.PositiveIntegerField(
        blank=False,
        null=True,
        verbose_name='Год выпуска ТС'
    )
    FrameNumber = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default='',
        verbose_name='Шасси (Рама) №'
    )
    EmptyMass = models.PositiveIntegerField(
        blank=False,
        null=True,
        verbose_name='Масса без нагрузки (кг)'
    )
    MaxMass = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name='Разрешенная максимальная масса (кг)'
    )
    Fuel = models.CharField(
        choices=FUEL_TYPES,
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Тип топлива'
    )
    BrakingSystem = models.CharField(
        choices=BRAKING_TYPES,
        max_length=15,
        blank=False,
        null=True,
        verbose_name='Тип привода тормозной системы'
    )
    Tyres = models.CharField(
        max_length=100,
        blank=False,
        default='',
        verbose_name='Марка шин'
    )
    Killometrage = models.PositiveIntegerField(
        blank=False,
        null=True,
        verbose_name='Пробег ТС (км)'
    )
    Make = models.CharField(
        max_length=100,
        blank=False,
        default='',
        verbose_name='Марка'
    )
    Model = models.CharField(
        max_length=100,
        blank=False,
        default='',
        verbose_name='Модель'
    )
    DocumentType = models.CharField(
        choices=DOCUMENT_TYPES,
        max_length=15,
        blank=False,
        null=True,
        verbose_name='Тип регистрационного документа'
    )
    Validity = models.PositiveIntegerField(
        choices=VALIDITY_VALUES,
        blank=False,
        null=True,
        verbose_name='Срок действия карты'
    )

    def __str__(self):
        return 'Транспортная карта №{}'.format(self.pk)

    def get_full_model(self):
        return '{} {}'.format(self.Make, self.Model)

    def get_payment_signature(self):
        return md5(':'.join((
            settings.ROBOKASSA['login'],
            str(self.payment.sum),
            str(self.payment.id),
            settings.ROBOKASSA['password1']
        )).encode()).hexdigest()

    def get_payment_url(self):
        return settings.PAYMENT_URL.format(
            login=settings.ROBOKASSA['login'],
            outsum=self.payment.sum,
            inv=self.payment.id,
            descr='Transport card pay',
            signature=self.get_payment_signature()
        )

    def create_payment(self):
        price = Price.objects.get(category=self.VehicleCategory)
        Payment.objects.create(card=self, sum=price.sum)

    class Meta:
        verbose_name = 'Транспортная карта'
        verbose_name_plural = 'Транспортные карты'
