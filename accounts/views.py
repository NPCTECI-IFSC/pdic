# encoding: utf-8
from accounts.forms import *
from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views import generic


class UsuarioCreate(generic.FormView):
    template_name = 'usuario_form.html'
    form_class = UsuarioForm
    success_url = 'index'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(UsuarioCreate, self).form_valid(form)


class LoginView(generic.FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = 'index'

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
