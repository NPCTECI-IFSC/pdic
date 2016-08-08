# encoding: utf-8
from __future__ import unicode_literals

from .forms import *
from .models import *
from django.core.urlresolvers import reverse
from django.views import generic


class Index(generic.TemplateView):
    template_name = 'index.html'


class TarefaForm(generic.FormView):
    template_name = 'tarefa_form.html'
    form_class = TarefaForm
    success_url = 'index'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            tarefa = form.save(commit=False)
            acao = Acao.objects.get(id=self.request.POST.get('acao'))
            tarefa.acao = acao
            tarefa.save()


class RotaForm(generic.FormView):
    template_name = 'generic_form.html'
    form_class = RotaForm
    success_url = 'index'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            form.save()


class VisaoForm(generic.FormView):
    template_name = 'generic_form.html'
    form_class = VisaoForm
    success_url = 'index'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            form.save()


class FatorForm(generic.FormView):
    template_name = 'generic_form.html'
    form_class = FatorForm
    success_url = 'index'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            form.save()


class ResponsavelForm(generic.FormView):
    template_name = 'generic_form.html'
    form_class = ResponsavelForm
    success_url = 'index'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            form.save()


class TemaForm(generic.FormView):
    template_name = 'generic_form.html'
    form_class = TemaForm
    success_url = 'index'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            form.save()


class AcaoForm(generic.FormView):
    template_name = 'generic_form.html'
    form_class = AcaoForm
    success_url = 'index'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            form.save()


class TarefaList(generic.ListView):
    template_name = 'generic_list.html'
    model = Tarefa


class RotaList(generic.ListView):
    template_name = 'generic_list.html'
    model = Rota


class VisaoList(generic.ListView):
    template_name = 'generic_list.html'
    model = Visao


class FatorList(generic.ListView):
    template_name = 'generic_list.html'
    model = Fator


class ResponsavelList(generic.ListView):
    template_name = 'generic_list.html'
    model = Responsavel


class UsuarioList(generic.ListView):
    template_name = 'generic_list.html'
    model = Usuario


class TemaList(generic.ListView):
    template_name = 'generic_list.html'
    model = Tema


class AcaoList(generic.ListView):
    template_name = 'generic_list.html'
    model = Acao
