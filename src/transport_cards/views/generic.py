# encoding: utf-8

from __future__ import unicode_literals

from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import Price, Insurance


class MainPageView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        data = super(MainPageView, self).get_context_data(**kwargs)

        data.update({
            'prices': Price.objects.all(),
        })
        return data


class ProfileView(LoginRequiredMixin, ListView):
    template_name = 'profile.html'
    context_object_name = 'cards'

    def get_queryset(self):
        return self.request.user.transport_cards.all()


class CouplePageView(TemplateView):
    template_name = 'couple.html'


class CheckBaseView(TemplateView):
    template_name = 'check-base.html'


class PaymentBenefitView(TemplateView):
    template_name = 'payment-benefit.html'


class InsuranceListView(ListView):
    model = Insurance
    context_object_name = 'insurance'
    template_name = 'insurance.html'