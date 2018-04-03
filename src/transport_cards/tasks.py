# encoding: utf-8

from __future__ import unicode_literals

from os.path import join

from django.core.mail import send_mail
from django.template.loader import get_template
from django.conf import settings

import requests
from requests.auth import HTTPBasicAuth
import pdfkit

from project.celery import app

from .models import TransportCard
from .serializers import TransportCardSerializer


@app.task
def send_email_to_new_user(email, password):
    message_params = {
        'host': settings.EMAIL_HOST_FOR_MAILS,
        'password': password
    }
    text = get_template('email/new_password.txt').render(message_params)
    html_text = get_template('email/new_password.html').render(message_params)

    send_mail(
        subject='Регистрация',
        message=text,
        html_message=html_text,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email]
    )


@app.task
def create_card_on_server(card_id):
    card = TransportCard.objects.get(pk=card_id)

    try:
        serializer = TransportCardSerializer(card)
        response = requests.post(
            settings.TO24_API['URL'],
            json=serializer.data,
            auth=HTTPBasicAuth(settings.TO24_API['LOGIN'],
                               settings.TO24_API['PASSWORD'])
        )

        if response.status_code != 200:
            raise ValueError('Запрос завершился c кодом {}'.format(response.status_code))

        data = response.json()
        if data.get('status', settings.TO24_API['FAIL']) != settings.TO24_API['SUCCESS']:
            raise ValueError('Запрос завершился неудачно. '
                             'Ответ сервера: {}'.format(data.get('text', response.text)))

        card.EAISTO_code = data['code']
        card.status = TransportCard.WAITING_RENDER
        card.exception = ''
        card.save()
        render_card_to_pdf.delay(card_id)

    except Exception as exception:
        card.status = TransportCard.SENDING_ERROR
        card.exception = exception
        card.save()


@app.task
def render_card_to_pdf(card_id):
    card = TransportCard.objects.get(pk=card_id)

    try:
        pdf_template = get_template('pdf_template.html').render({
            'card': card
        })
        local_pdf_path = join('pdf', 'transport_card_{}.pdf'.format(card.pk))
        pdf_path = join(settings.MEDIA_ROOT, local_pdf_path)

        pdfkit.from_string(pdf_template, pdf_path)

        card.pdf = local_pdf_path
        card.status = TransportCard.READY
        card.exception = ''
        card.save()
        notify_user.delay(card.user.email)

    except Exception as exception:
        card.status = TransportCard.RENDER_ERROR
        card.exception = exception
        card.save()


@app.task
def notify_user(email):
    message_params = {
        'host': settings.EMAIL_HOST_FOR_MAILS
    }
    text = get_template('email/card_created.txt').render(message_params)
    html_text = get_template('email/card_created.html').render(message_params)

    send_mail(
        subject='Транспортная карта готова',
        message=text,
        html_message=html_text,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email]
    )
