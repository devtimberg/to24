# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-22 10:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='Email')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u0410\u043a\u0442\u0438\u0432\u0435\u043d')),
                ('is_staff', models.BooleanField(default=False, verbose_name='\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c',
                'verbose_name_plural': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f')),
                ('sum', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, verbose_name='\u0421\u0443\u043c\u043c\u0430 \u043f\u043b\u0430\u0442\u0435\u0436\u0430')),
            ],
            options={
                'verbose_name': '\u041f\u043b\u0430\u0442\u0435\u0436',
                'verbose_name_plural': '\u041f\u043b\u0430\u0442\u0435\u0436\u0438',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='\u0426\u0435\u043d\u0430')),
                ('category', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=1, null=True, unique=True, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u0426\u0435\u043d\u043d\u0438\u043a',
                'verbose_name_plural': '\u0426\u0435\u043d\u043d\u0438\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='TransportCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f')),
                ('phone', models.CharField(max_length=25, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('status', models.SmallIntegerField(blank=True, choices=[(0, '\u041e\u0436\u0438\u0434\u0430\u0435\u0442 \u043e\u043f\u043b\u0430\u0442\u044b'), (1, '\u041e\u0436\u0438\u0434\u0430\u0435\u0442 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f'), (2, '\u041e\u0436\u0438\u0434\u0430\u0435\u0442 \u0440\u0435\u043d\u0434\u0435\u0440\u0430'), (3, '\u0413\u043e\u0442\u043e\u0432\u0430'), (4, '\u041e\u0448\u0438\u0431\u043a\u0430 \u043f\u0440\u0438 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438 \u043a\u0430\u0440\u0442\u044b'), (5, '\u041e\u0448\u0438\u0431\u043a\u0430 \u043f\u0440\u0438 \u0440\u0435\u043d\u0434\u0435\u0440\u0435')], default=0, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441')),
                ('exception', models.TextField(blank=True, default='', verbose_name='\u0418\u0441\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdf/', verbose_name='PDF')),
                ('FName', models.CharField(default='', max_length=100, verbose_name='\u0418\u043c\u044f')),
                ('Name', models.CharField(default='', max_length=100, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('MName', models.CharField(blank=True, default='', max_length=100, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e')),
                ('Series', models.CharField(default='', max_length=100, verbose_name='\u0421\u0435\u0440\u0438\u044f')),
                ('Number', models.PositiveIntegerField(null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440')),
                ('Organization', models.CharField(default='', max_length=100, verbose_name='\u0412\u044b\u0434\u0430\u043d \u043a\u0435\u043c')),
                ('Date', models.DateField(null=True, verbose_name='\u0412\u044b\u0434\u0430\u043d \u043a\u043e\u0433\u0434\u0430')),
                ('Foreign', models.BooleanField(default=False, verbose_name='\u0418\u043d\u043e\u0441\u0442\u0440\u0430\u043d\u043d\u044b\u0439 \u0433\u0440\u0430\u0436\u0434\u0430\u043d\u0438\u043d')),
                ('specials', models.CharField(blank=True, choices=[('taxi', '\u042f\u0432\u043b\u044f\u0435\u0442\u0441\u044f c\u043f\u0435\u0446\u0442\u0435\u0445\u043d\u0438\u043a\u043e\u0439 \u0438\u043b\u0438 \u0442\u0430\u043a\u0441\u0438'), ('MVD', '\u042f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0443\u0447\u0435\u0431\u043d\u043e\u0439 \u0438\u043b\u0438 \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u0438\u0442 \u0413\u0418\u0411\u0414\u0414 \u0438\u043b\u0438 \u041c\u0412\u0414')], max_length=4, null=True, verbose_name='\u041e\u0441\u043e\u0431\u0435\u043d\u043d\u043e\u0441\u0442\u044c \u0422\u0421')),
                ('EAISTO_code', models.CharField(blank=True, default='', max_length=21, verbose_name='\u041a\u043e\u0434 \u0415\u0410\u0418\u0421\u0422\u041e')),
                ('BodyNumber', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='\u041a\u0443\u0437\u043e\u0432 \u2116')),
                ('Note', models.TextField(blank=True, default='', verbose_name='\u0417\u0430\u043c\u0435\u0447\u0430\u043d\u0438\u044f')),
                ('RegistrationNumber', models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='\u0413\u043e\u0441\u0443\u0434\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0437\u043d\u0430\u043a')),
                ('VehicleCategory', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=1, null=True, verbose_name='\u0421\u0420\u0422\u0421 \u0438\u043b\u0438 \u041f\u0422\u0421')),
                ('VehicleCategory2', models.CharField(choices=[('A', (('L', '\u041c\u043e\u0442\u043e\u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442 L'),)), ('B', (('M1', '\u041b\u0435\u0433\u043a\u043e\u0432\u043e\u0439 M1'), ('N1', '\u0413\u0440\u0443\u0437\u043e\u0432\u043e\u0439 \u0434\u043e 3.5 \u0442\u043e\u043d\u043d N1'))), ('C', (('N2', '\u0413\u0440\u0443\u0437\u043e\u0432\u043e\u0439 \u0434\u043e 12 \u0442\u043e\u043d\u043d N2'), ('N3', '\u0413\u0440\u0443\u0437\u043e\u0432\u043e\u0439 \u0431\u043e\u043b\u0435\u0435 12 \u0442\u043e\u043d\u043d N3'))), ('D', (('M2', '\u0410\u0432\u0442\u043e\u0431\u0443\u0441\u044b \u0434\u043e 5 \u0442\u043e\u043d\u043d M2'), ('M3', '\u0410\u0432\u0442\u043e\u0431\u0443\u0441\u044b \u0431\u043e\u043b\u0435\u0435 5 \u0442\u043e\u043d\u043d M3'))), ('E', (('O1', '\u041f\u0440\u0438\u0446\u0435\u043f\u044b \u0434\u043e 150 \u043a\u0433 O1'), ('O2', '\u041f\u0440\u0438\u0446\u0435\u043f\u044b \u0434\u043e 3.5 \u0442\u043e\u043d\u043d O2'), ('O3', '\u041f\u0440\u0438\u0446\u0435\u043f\u044b \u0434\u043e 10 \u0442\u043e\u043d\u043d O3'), ('O4', '\u041f\u0440\u0438\u0446\u0435\u043f\u044b \u0431\u043e\u043b\u0435\u0435 10 \u0442\u043e\u043d\u043d O4')))], default='B', max_length=2, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0422\u0421 (\u041e\u041a\u041f)')),
                ('VIN', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='VIN')),
                ('Year', models.PositiveIntegerField(null=True, verbose_name='\u0413\u043e\u0434 \u0432\u044b\u043f\u0443\u0441\u043a\u0430 \u0422\u0421')),
                ('FrameNumber', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='\u0428\u0430\u0441\u0441\u0438 (\u0420\u0430\u043c\u0430) \u2116')),
                ('EmptyMass', models.PositiveIntegerField(null=True, verbose_name='\u041c\u0430\u0441\u0441\u0430 \u0431\u0435\u0437 \u043d\u0430\u0433\u0440\u0443\u0437\u043a\u0438 (\u043a\u0433)')),
                ('MaxMass', models.PositiveIntegerField(blank=True, null=True, verbose_name='\u0420\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u043d\u0430\u044f \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u043c\u0430\u0441\u0441\u0430 (\u043a\u0433)')),
                ('Fuel', models.CharField(blank=True, choices=[(None, '\u0411\u0435\u0437 \u0442\u043e\u043f\u043b\u0438\u0432\u0430'), ('Petrol', '\u0411\u0435\u043d\u0437\u0438\u043d'), ('Diesel', '\u0414\u0438\u0437\u0435\u043b\u044c\u043d\u043e\u0435 \u0442\u043e\u043f\u043b\u0438\u0432\u043e'), ('PressureGas', 'C\u0436\u0430\u0442\u044b\u0439 \u0433\u0430\u0437'), ('LiquefiedGas', '\u0421\u0436\u0438\u0436\u0435\u043d\u043d\u044b\u0439 \u0433\u0430\u0437')], max_length=15, null=True, verbose_name='\u0422\u0438\u043f \u0442\u043e\u043f\u043b\u0438\u0432\u0430')),
                ('BrakingSystem', models.CharField(choices=[(None, '\u0411\u0435\u0437 \u0442\u043e\u0440\u043c\u043e\u0437\u043d\u043e\u0439 \u0441\u0438\u0441\u0442\u0435\u043c\u044b'), ('Mechanical', '\u041c\u0435\u0445\u0430\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0439'), ('Hydraulic', '\u0413\u0438\u0434\u0440\u0430\u0432\u043b\u0438\u0447\u0435\u0441\u043a\u0438\u0439'), ('Pneumatic', '\u041f\u043d\u0435\u0432\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439'), ('Combined', '\u041a\u043e\u043c\u0431\u0438\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439')], max_length=15, null=True, verbose_name='\u0422\u0438\u043f \u043f\u0440\u0438\u0432\u043e\u0434\u0430 \u0442\u043e\u0440\u043c\u043e\u0437\u043d\u043e\u0439 \u0441\u0438\u0441\u0442\u0435\u043c\u044b')),
                ('Tyres', models.CharField(default='', max_length=100, verbose_name='\u041c\u0430\u0440\u043a\u0430 \u0448\u0438\u043d')),
                ('Killometrage', models.PositiveIntegerField(null=True, verbose_name='\u041f\u0440\u043e\u0431\u0435\u0433 \u0422\u0421 (\u043a\u043c)')),
                ('Make', models.CharField(default='', max_length=100, verbose_name='\u041c\u0430\u0440\u043a\u0430')),
                ('Model', models.CharField(default='', max_length=100, verbose_name='\u041c\u043e\u0434\u0435\u043b\u044c')),
                ('DocumentType', models.CharField(choices=[('RegTalon', '\u0421\u0432\u0438\u0434\u0435\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u043e  \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043d\u043e\u0433\u043e \u0441\u0440\u0435\u0434\u0441\u0442\u0432\u0430'), ('PTS', '\u041f\u0430\u0441\u043f\u043e\u0440\u0442 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043d\u043e\u0433\u043e \u0441\u0440\u0435\u0434\u0441\u0442\u0432\u0430')], max_length=15, null=True, verbose_name='\u0422\u0438\u043f \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u043e\u0433\u043e \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430')),
                ('Validity', models.PositiveIntegerField(choices=[(6, '6'), (12, '12'), (24, '24')], null=True, verbose_name='\u0421\u0440\u043e\u043a \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u043a\u0430\u0440\u0442\u044b')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transport_cards', to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c')),
            ],
            options={
                'verbose_name': '\u0422\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043d\u0430\u044f \u043a\u0430\u0440\u0442\u0430',
                'verbose_name_plural': '\u0422\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043d\u044b\u0435 \u043a\u0430\u0440\u0442\u044b',
            },
        ),
        migrations.AddField(
            model_name='payment',
            name='card',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='transport_cards.TransportCard', verbose_name='\u041d\u043e\u043c\u0435\u0440 \u043f\u043b\u0430\u0442\u0435\u0436\u0430'),
        ),
    ]
