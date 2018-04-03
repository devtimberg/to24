# encoding: utf-8

from __future__ import unicode_literals

from django.contrib.auth import REDIRECT_FIELD_NAME, views
from django.shortcuts import resolve_url
from django.utils.http import is_safe_url
from django.conf import settings


class SafeNextUrlMixin(views.SuccessURLAllowedHostsMixin):
    redirect_field_name = REDIRECT_FIELD_NAME

    def get_success_url(self):
        """Ensure the user-originating redirection URL is safe."""
        redirect_to = self.request.POST.get(
            self.redirect_field_name,
            self.request.GET.get(self.redirect_field_name, '')
        )
        if not redirect_to:
            return super(SafeNextUrlMixin, self).get_success_url()

        url_is_safe = is_safe_url(
            url=redirect_to,
            allowed_hosts=self.get_success_url_allowed_hosts(),
            require_https=self.request.is_secure(),
        )
        if not url_is_safe:
            return resolve_url(settings.LOGIN_REDIRECT_URL)
        return redirect_to
