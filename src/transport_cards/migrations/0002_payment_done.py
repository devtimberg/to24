# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-22 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport_cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='done',
            field=models.BooleanField(default=False, verbose_name='\u041f\u043b\u0430\u0442\u0435\u0436 \u043f\u0440\u0438\u043d\u044f\u0442'),
        ),
    ]