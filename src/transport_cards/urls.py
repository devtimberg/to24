# encoding: utf-8

from __future__ import unicode_literals

from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^$', MainPageView.as_view(), name='main'),

    url(r'^couple/$', CouplePageView.as_view(), name='couple'),
    url(r'^check-base/$', CheckBaseView.as_view(), name='check-base'),
    url(r'^payment-benefit/$', PaymentBenefitView.as_view(), name='payment-benefit'),
    url(r'^insurance/$', InsuranceListView.as_view(), name='insurance'),

    url(r'^profile/$', ProfileView.as_view(), name='profile'),
    url(r'^cards/create/$', CreateCardView.as_view(), name='create_card'),
    url(r'^payment-result/$', PaymentResultView.as_view(), name='payment_result'),

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^restore-password/$', RestorePasswordView.as_view(), name='restore_password'),
]
