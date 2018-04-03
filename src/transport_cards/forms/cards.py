# encoding: utf-8

from __future__ import unicode_literals

from datetime import datetime

from django import forms
from django.contrib import messages

from ..models import TransportCard, User, Price, CATEGORIES
from ..tasks import send_email_to_new_user


class CreateCardForm(forms.ModelForm):

    def __init__(self, **kwargs):
        self.user = kwargs.pop('user')
        self.request = kwargs.pop('request')
        super(CreateCardForm, self).__init__(**kwargs)

    def clean_Year(self):
        if self.cleaned_data['Year'] > datetime.today().year:
            raise forms.ValidationError('Указанный год больше текущего')
        return self.cleaned_data['Year']

    def save(self, commit=True):
        user = self.user

        new_card = super(CreateCardForm, self).save(commit=False)
        new_card.user = user

        # Правильное выставление категории вида A, B, C, D, E
        new_card.VehicleCategory = CATEGORIES.LINKED[new_card.VehicleCategory2]

        # Выставление срока годности карты
        specials = self.cleaned_data.get('specials')
        if specials:
            if specials == 'taxi':
                new_card.Validity = 6
            elif specials == 'MVD':
                new_card.Validity = 12
        elif datetime.today().year - self.cleaned_data['Year'] < 3:
            new_card.Validity = 24
        else:
            new_card.Validity = 12

        # Выставление цены за карту в зависимости от категории
        price = Price.objects.get(category=new_card.VehicleCategory)
        new_card.payment_sum = price.sum

        if commit:
            new_card.save()

        return new_card

    class Meta:
        model = TransportCard
        fields = (
            # Паспортные данные
            'FName', 'Name', 'MName', 'Series', 'Number',
            'Organization', 'Date', 'Foreign', 'phone',

            # Данные о ТС
            'Number', 'BodyNumber', 'Note', 'RegistrationNumber',
            'VIN', 'Year', 'FrameNumber', 'EmptyMass', 'MaxMass',
            'Fuel', 'Tyres', 'BrakingSystem', 'Killometrage',
            'Make', 'Model', 'DocumentType', 'specials',
            'VehicleCategory2',
        )


class CreateCardWithUserForm(CreateCardForm):
    email = forms.EmailField(required=True)

    def get_or_create_user(self):
        try:
            user = User.objects.get(email=self.cleaned_data['email'])
        except User.DoesNotExist:
            user = User(email=self.cleaned_data['email'])
            user.set_random_password()
            user.save()

            # Отправка почты с паролем новому юзеру
            send_email_to_new_user.delay(email=user.email, password=user.raw_password)

            messages.success(self.request, '''
                Ваш аккаунт зарегистрирован, на указанную почту
                отправлено письмо с паролем
            ''')
        return user

    def save(self, commit=True):
        self.user = self.get_or_create_user()
        return super(CreateCardForm, self).save(commit=commit)
