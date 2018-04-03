# encoding: utf-8

from __future__ import unicode_literals

from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from django.contrib.messages.views import SuccessMessageMixin

from ..forms import CreateCardForm, CreateCardWithUserForm


class CreateCardView(SuccessMessageMixin, CreateView):
    template_name = 'create_card.html'
    success_message = 'Ваша заявка успешно принята в обработку и ожидает оплаты в Личном кабинете'

    def get_form_class(self):
        if self.request.user.is_authenticated:
            return CreateCardForm
        else:
            return CreateCardWithUserForm

    def get_form_kwargs(self):
        kwargs = super(CreateCardView, self).get_form_kwargs()
        kwargs.update({
            'request': self.request,
            'user': self.request.user
        })
        return kwargs

    def get_success_url(self):
        form_user_email = self.get_form_kwargs()['data'].get('email')

        if self.request.user.is_authenticated:
            return self.object.get_payment_url()

        return '{}?email={}'.format(reverse('login'), form_user_email)
