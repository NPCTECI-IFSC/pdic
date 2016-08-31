# encoding: utf-8
from __future__ import unicode_literals

from accounts.forms import *
from accounts.models import *
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


class ResponsavelList(generic.ListView):
    template_name = 'responsavel_list.html'
    context_object_name = 'responsaveis'
    model = Responsavel
    paginate_by = 15

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        query = Responsavel.objects.all()
        if not self.request.user.is_authenticated():
            query = query.filter(ativa=True)
        if q:
            query = query.filter(nome__icontains=q)
        return query


class ResponsavelCreate(generic.FormView):
    template_name = 'generic_form.html'
    form_class = ResponsavelForm
    success_url = 'accounts:list-responsaveis'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(ResponsavelCreate, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(
            ResponsavelCreate, self
        ).get_context_data(*args, **kwargs)
        context['nome_form'] = u'Cadastro de responsável'
        return context


class ResponsavelEdit(generic.UpdateView):
    template_name = 'generic_form.html'
    form_class = ResponsavelForm
    model = Responsavel
    success_url = 'accounts:list-responsaveis'

    def get_success_url(self):
        return reverse(self.success_url)

    def get_context_data(self, *args, **kwargs):
        context = super(
            ResponsavelEdit, self
        ).get_context_data(*args, **kwargs)
        context['nome_form'] = u'Edição de responsável'
        return context


class ResponsavelDelete(generic.edit.DeleteView):
    template_name = 'generic_delete.html'
    model = Responsavel
    success_url = 'accounts:list-responsaveis'

    def get_success_url(self):
        return reverse(self.success_url)
