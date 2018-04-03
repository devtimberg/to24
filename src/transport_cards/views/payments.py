# encoding: utf-8

from __future__ import unicode_literals

import logging

from django.views.generic import View
from django.http import HttpResponse, HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from ..models import TransportCard
from ..forms import PaymentResultForm
from ..tasks import create_card_on_server


@method_decorator(csrf_exempt, name='dispatch')
class PaymentResultView(View):
    """
    Принимает запрос с результатами оплаты от робокассы,
    создает таску на рендер в случае успеха,
    пишет ошибки в логгер робокассы в случае неуспеха
    """

    http_method_names = ['get', 'post']

    def __init__(self, **kwargs):
        self.logger = logging.getLogger('robokassa')
        super(PaymentResultView, self).__init__(**kwargs)

    def post(self, request, *args, **kwargs):
        return self.process_form(request.POST)

    def get(self, request, *args, **kwargs):
        return self.process_form(request.GET)

    def process_form(self, form_data):
        form = PaymentResultForm(form_data)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        card = form.payment.card
        card.status = TransportCard.WAITING_REQUEST
        card.save()

        create_card_on_server.delay(card.id)
        return HttpResponse('OK%s\n' % form.cleaned_data['InvId'])

    def form_invalid(self, form):
        self.logger.error('Errors: %s' % form.errors)
        return HttpResponseBadRequest()
