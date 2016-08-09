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
    success_url = 'pdic:list-tarefas'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(TarefaForm, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(TarefaForm, self).get_context_data(*args, **kwargs)
        context['nome_form'] = 'tarefas'
        return context


class RotaForm(generic.FormView):
    template_name = 'generic_form.html'
    form_class = RotaForm
    success_url = 'pdic:list-rotas'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(RotaForm, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RotaForm, self).get_context_data(*args, **kwargs)
        context['nome_form'] = 'rotas'
        return context


class VisaoForm(generic.FormView):
    template_name = 'generic_form.html'
    form_class = VisaoForm
    success_url = 'pdic:list-visoes'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(VisaoForm, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(VisaoForm, self).get_context_data(*args, **kwargs)
        context['nome_form'] = u'visões'
        return context


class FatorForm(generic.FormView):
    template_name = 'generic_form.html'
    form_class = FatorForm
    success_url = 'pdic:list-fatores'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(FatorForm, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(FatorForm, self).get_context_data(*args, **kwargs)
        context['nome_form'] = 'fatores'
        return context


class ResponsavelForm(generic.FormView):
    template_name = 'generic_form.html'
    form_class = ResponsavelForm
    success_url = 'pdic:list-responsaveis'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(ResponsavelForm, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ResponsavelForm, self).get_context_data(*args, **kwargs)
        context['nome_form'] = u'responsáveis'
        return context


class TemaForm(generic.FormView):
    template_name = 'generic_form.html'
    form_class = TemaForm
    success_url = 'pdic:list-temas'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(TemaForm, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(TemaForm, self).get_context_data(*args, **kwargs)
        context['nome_form'] = 'temas'
        return context


class AcaoForm(generic.FormView):
    template_name = 'generic_form.html'
    form_class = AcaoForm
    success_url = 'pdic:list-acoes'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(AcaoForm, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(AcaoForm, self).get_context_data(*args, **kwargs)
        context['nome_form'] = u'ações'
        return context


class TarefaList(generic.ListView):
    template_name = 'tarefa_list.html'
    context_object_name = 'tarefas'
    model = Tarefa
    paginate_by = 15


class RotaList(generic.ListView):
    template_name = 'rota_list.html'
    context_object_name = 'rotas'
    model = Rota
    paginate_by = 15


class VisaoList(generic.ListView):
    template_name = 'visao_list.html'
    context_object_name = 'visoes'
    model = Visao
    paginate_by = 15


class FatorList(generic.ListView):
    template_name = 'fator_list.html'
    context_object_name = 'fatores'
    model = Fator
    paginate_by = 15


class ResponsavelList(generic.ListView):
    template_name = 'responsavel_list.html'
    context_object_name = 'responsaveis'
    model = Responsavel
    paginate_by = 15


class TemaList(generic.ListView):
    template_name = 'tema_list.html'
    context_object_name = 'temas'
    model = Tema
    paginate_by = 15


class AcaoList(generic.ListView):
    template_name = 'acao_list.html'
    context_object_name = 'acoes'
    model = Acao
    paginate_by = 10
