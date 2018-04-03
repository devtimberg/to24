# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-26 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport_cards', '0003_insurance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='price',
            options={'ordering': ['order'], 'verbose_name': 'Ценник', 'verbose_name_plural': 'Ценники'},
        ),
        migrations.AddField(
            model_name='price',
            name='order',
            field=models.PositiveIntegerField(default=0, help_text='Отсчет начинается с "0"', verbose_name='Порядок'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='logotype',
            field=models.ImageField(upload_to='insurance', verbose_name='Логотип компании'),
        ),
    ]