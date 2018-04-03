# encoding: utf-8

from __future__ import unicode_literals

from django.apps import AppConfig
from django.db.models.signals import post_save

from .signals import create_payment


class CoreConfig(AppConfig):
    name = 'transport_cards'
    verbose_name = 'Транспортные карты'

    def ready(self):
        TransportCard = self.get_model('TransportCard')
        post_save.connect(create_payment, TransportCard)
