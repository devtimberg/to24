# encoding: utf-8

from __future__ import unicode_literals

from hashlib import md5

from django import forms
from django.conf import settings

from ..models import Payment


class PaymentResultForm(forms.Form):
    InvId = forms.IntegerField(
        min_value=1,
        required=True,
    )
    OutSum = forms.DecimalField(
        required=True,
    )
    SignatureValue = forms.CharField(
        max_length=100,
        required=True,
    )
    card = None

    def clean_InvId(self):
        payment_id = self.cleaned_data.get('InvId')
        if not payment_id:
            raise forms.ValidationError('Не указан ID платежа')
        try:
            self.payment = Payment.objects.get(pk=payment_id)
        except Payment.DoesNotExist:
            raise forms.ValidationError('Платеж с таким ID({}) не найден в базе'
                                        .format(payment_id))
        return payment_id

    def clean(self):
        if self.errors:
            return
        data = self.cleaned_data

        if self.payment.done:
            raise forms.ValidationError('Эта оплата уже проведена')

        if self.payment.sum != data['OutSum']:
            raise forms.ValidationError('Суммы не совпадают')

        crc_sum = md5(':'.join(
            (
                str(data['OutSum']),
                str(data['InvId']),
                settings.ROBOKASSA['password2'],
            )
        ).encode()).hexdigest().upper()
        if crc_sum != data['SignatureValue']:
            raise forms.ValidationError('Сигнатуры не совпадают')

    def save(self):
        self.payment.done = True
        self.payment.save()
