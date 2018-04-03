# encoding: utf-8

from __future__ import unicode_literals

from django.views.generic import RedirectView, FormView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import logout
from django.contrib import messages

from .mixins import SafeNextUrlMixin

from ..forms import LoginForm, RestorePasswordForm
from ..tasks import send_email_to_new_user


class LoginView(SafeNextUrlMixin, FormView):
    template_name = 'auth/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('profile')

    def get_initial(self):
        return self.request.GET

    def form_valid(self, form):
        form.auth(self.request)
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return reverse('main')


class RestorePasswordView(FormView):
    template_name = 'auth/restore_password.html'
    form_class = RestorePasswordForm
    user = None

    def form_valid(self, form):
        self.user = form.user
        self.user.set_random_password()
        self.user.save()
        send_email_to_new_user.delay(email=self.user.email, password=self.user.raw_password)
        messages.success(self.request, 'На указанную почту отправлено письмо с паролем')
        return super(RestorePasswordView, self).form_valid(form)

    def get_success_url(self):
        return '{}?email={}'.format(reverse('login'), self.user.email)
