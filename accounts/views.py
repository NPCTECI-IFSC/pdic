# encoding: utf-8
from __future__ import unicode_literals

from accounts.forms import *
from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views import generic


class LoginView(generic.FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = 'index'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect(reverse(self.success_url))
        else:
            return super(LoginView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            user = authenticate(
                username=self.request.POST.get('email'),
                password=self.request.POST.get('password')
            )
            login(self.request, user)
        return super(LoginView, self).form_valid(form)


def logout_view(request):
    logout(request)
    return redirect(reverse('index'))
