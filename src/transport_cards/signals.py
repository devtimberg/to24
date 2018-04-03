# encoding: utf-8

from __future__ import unicode_literals


def create_payment(sender, instance, created, **kwargs):
    if created:
        instance.create_payment()
