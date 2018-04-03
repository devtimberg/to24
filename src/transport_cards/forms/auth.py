# encoding: utf-8

from __future__ import unicode_literals

from django import forms
from django.contrib.auth import authenticate, login

from ..models import User


class LoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
    )
    password = forms.CharField(
        required=True,
    )
    user = None

    def clean(self):
        self.user = authenticate(**self.cleaned_data)

        if self.user is None:
            raise forms.ValidationError('Пользователь с такими данными не зарегистрирован')

        elif not self.user.is_active:
            raise forms.ValidationError('Этот аккаунт заблокирован')

    def auth(self, request):
        login(request, self.user)


class RestorePasswordForm(forms.Form):
    email = forms.EmailField(
        required=True,
    )
    user = None

    def clean_email(self):
        try:
            self.user = User.objects.get(email=self.cleaned_data['email'])
        except User.DoesNotExist:
            raise forms.ValidationError('Пользователя с таким email не существует')
        return self.cleaned_data['email']
