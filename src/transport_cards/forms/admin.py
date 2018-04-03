# encoding: utf-8

from __future__ import unicode_literals

from django import forms

from ..models import User


class AbstractUserForm(forms.ModelForm):
    new_password = forms.CharField(
        label='Новый пароль',
        required=False,
        widget=forms.PasswordInput
    )
    password_repeat = forms.CharField(
        label='Повторите пароль',
        required=False,
        widget=forms.PasswordInput
    )

    def clean(self):
        new_password = self.cleaned_data.get('new_password')
        password_repeat = self.cleaned_data.get('password_repeat')
        if new_password and password_repeat and new_password != password_repeat:
            raise forms.ValidationError('Пароли не совпадают')

    class Meta:
        model = User
        fields = (
            'email',
            'is_active',
            'is_staff',
            'is_superuser',
        )


class UserChangeForm(AbstractUserForm):
    """
    Form for updating user data
    """

    def save(self, commit=True):
        user = super(UserChangeForm, self).save(commit=False)

        # Добавление пользователя в новые группы
        for group in self.cleaned_data.get('groups', []):
            if not user.groups.all().filter(name=group.name).exists():
                user.groups.add(group)

        new_password = self.cleaned_data["new_password"]
        if new_password and len(new_password) != 0:
            user.set_password(new_password)

        if commit:
            user.save()

        return user


class UserAddForm(AbstractUserForm):
    """
    Форма для создания пользователей из админки
    """

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Не указана почта')
        elif User.objects.filter(email=email).exists():
            raise forms.ValidationError('Эта почта уже занята')
        return email

    def save(self, commit=True):
        user = super(UserAddForm, self).save(commit=False)
        user.set_password(self.cleaned_data['new_password'])

        if commit:
            user.save()

        return user
