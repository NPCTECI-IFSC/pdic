# encoding: utf-8
from __future__ import unicode_literals

from .forms import *
from .models import *
from django.db.models import Sum, Count, ExpressionWrapper, FloatField
from django.core.urlresolvers import reverse
from django.views import generic


class Index(generic.TemplateView):
    template_name = 'index.html'


class TarefaList(generic.ListView):
    template_name = 'tarefa_list.html'
    context_object_name = 'tarefas'
    model = Tarefa
    paginate_by = 15

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        query = Tarefa.objects.all()
        if not self.request.user.is_authenticated():
            query = query.filter(ativa=True)
        if q:
            query = query.filter(descricao__icontains=q)
        return query


class TarefaCreate(generic.FormView):
    template_name = 'tarefa_form.html'
    form_class = TarefaForm
    success_url = 'pdic:list-tarefas'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(TarefaCreate, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(TarefaCreate, self).get_context_data(*args, **kwargs)
        context['nome_form'] = 'Cadastro de tarefa'
        return context


class TarefaEdit(generic.edit.UpdateView):
    template_name = 'tarefa_form.html'
    form_class = TarefaForm
    model = Tarefa
    success_url = 'pdic:list-tarefas'

    def get_success_url(self):
        return reverse(self.success_url)

    def get_context_data(self, *args, **kwargs):
        context = super(TarefaEdit, self).get_context_data(*args, **kwargs)
        context['nome_form'] = u'Edição de tarefa'
        return context


class TarefaDelete(generic.edit.DeleteView):
    template_name = 'generic_delete.html'
    model = Tarefa
    success_url = 'pdic:list-tarefas'

    def get_success_url(self):
        return reverse(self.success_url)


class RotaList(generic.ListView):
    template_name = 'rota_list.html'
    context_object_name = 'rotas'
    model = Rota
    paginate_by = 15

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        query = Rota.objects.all()
        if not self.request.user.is_authenticated():
            query = query.filter(ativa=True)
        if q:
            query = query.filter(nome__icontains=q)
        return query


class RotaCreate(generic.FormView):
    template_name = 'generic_form.html'
    form_class = RotaForm
    success_url = 'pdic:list-rotas'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(RotaCreate, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RotaCreate, self).get_context_data(*args, **kwargs)
        context['nome_form'] = 'Cadastro de rota'
        return context


class RotaEdit(generic.edit.UpdateView):
    template_name = 'generic_form.html'
    form_class = RotaForm
    model = Rota
    success_url = 'pdic:list-rotas'

    def get_success_url(self):
        return reverse(self.success_url)

    def get_context_data(self, *args, **kwargs):
        context = super(RotaEdit, self).get_context_data(*args, **kwargs)
        context['nome_form'] = u'Edição de rota'
        return context


class RotaDelete(generic.edit.DeleteView):
    template_name = 'generic_delete.html'
    model = Rota
    success_url = 'pdic:list-rotas'

    def get_success_url(self):
        return reverse(self.success_url)


class VisaoList(generic.ListView):
    template_name = 'visao_list.html'
    context_object_name = 'visoes'
    model = Visao
    paginate_by = 15

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        query = Visao.objects.all()
        if not self.request.user.is_authenticated():
            query = query.filter(ativa=True)
        if q:
            query = query.filter(descricao__icontains=q)
        return query


class VisaoCreate(generic.FormView):
    template_name = 'generic_form.html'
    form_class = VisaoForm
    success_url = 'pdic:list-visoes'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(VisaoCreate, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(VisaoCreate, self).get_context_data(*args, **kwargs)
        context['nome_form'] = u'Cadastro de visão'
        return context


class VisaoEdit(generic.edit.UpdateView):
    template_name = 'generic_form.html'
    form_class = VisaoForm
    model = Visao
    success_url = 'pdic:list-visoes'

    def get_success_url(self):
        return reverse(self.success_url)

    def get_context_data(self, *args, **kwargs):
        context = super(VisaoEdit, self).get_context_data(*args, **kwargs)
        context['nome_form'] = u'Edição de visão'
        return context


class VisaoDelete(generic.edit.DeleteView):
    template_name = 'generic_delete.html'
    model = Visao
    success_url = 'pdic:list-visoes'

    def get_success_url(self):
        return reverse(self.success_url)


class FatorList(generic.ListView):
    template_name = 'fator_list.html'
    context_object_name = 'fatores'
    model = Fator
    paginate_by = 15

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        query = Fator.objects.all()
        if not self.request.user.is_authenticated():
            query = query.filter(ativa=True)
        if q:
            query = query.filter(nome__icontains=q)
        return query


class FatorCreate(generic.FormView):
    template_name = 'generic_form.html'
    form_class = FatorForm
    success_url = 'pdic:list-fatores'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(FatorCreate, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(FatorCreate, self).get_context_data(*args, **kwargs)
        context['nome_form'] = 'Cadastro de fator'
        return context


class FatorEdit(generic.edit.UpdateView):
    template_name = 'generic_form.html'
    form_class = FatorForm
    model = Fator
    success_url = 'pdic:list-fatores'

    def get_success_url(self):
        return reverse(self.success_url)

    def get_context_data(self, *args, **kwargs):
        context = super(FatorEdit, self).get_context_data(*args, **kwargs)
        context['nome_form'] = u'Edição de fator'
        return context


class FatorDelete(generic.edit.DeleteView):
    template_name = 'generic_delete.html'
    model = Fator
    success_url = 'pdic:list-fatores'

    def get_success_url(self):
        return reverse(self.success_url)


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
    success_url = 'pdic:list-responsaveis'

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
    success_url = 'pdic:list-responsaveis'

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
    success_url = 'pdic:list-responsaveis'

    def get_success_url(self):
        return reverse(self.success_url)


class TemaList(generic.ListView):
    template_name = 'tema_list.html'
    context_object_name = 'temas'
    model = Tema
    paginate_by = 15

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        query = Tema.objects.all()
        if not self.request.user.is_authenticated():
            query = query.filter(ativa=True)
        if q:
            query = query.filter(descricao__icontains=q)
        return query


class TemaCreate(generic.FormView):
    template_name = 'generic_form.html'
    form_class = TemaForm
    success_url = 'pdic:list-temas'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(TemaCreate, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(TemaCreate, self).get_context_data(*args, **kwargs)
        context['nome_form'] = 'Cadastro de tema'
        return context


class TemaEdit(generic.edit.UpdateView):
    template_name = 'generic_form.html'
    form_class = TemaForm
    model = Tema
    success_url = 'pdic:list-temas'

    def get_success_url(self):
        return reverse(self.success_url)

    def get_context_data(self, *args, **kwargs):
        context = super(TemaEdit, self).get_context_data(*args, **kwargs)
        context['nome form'] = u'Edição de tema'
        return context


class TemaDelete(generic.edit.DeleteView):
    template_name = 'generic_delete.html'
    model = Tema
    success_url = 'pdic:list-temas'

    def get_success_url(self):
        return reverse(self.success_url)


class AcaoList(generic.ListView):
    template_name = 'acao_list.html'
    context_object_name = 'acoes'
    model = Acao
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        query = Acao.objects.all()
        if not self.request.user.is_authenticated():
            query = query.filter(ativa=True)
        if q:
            query = query.filter(descricao__icontains=q)
        return query


class AcaoCreate(generic.FormView):
    template_name = 'generic_form.html'
    form_class = AcaoForm
    success_url = 'pdic:list-acoes'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(AcaoCreate, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(AcaoCreate, self).get_context_data(*args, **kwargs)
        context['nome_form'] = u'Cadastro de ação'
        return context


class AcaoEdit(generic.edit.UpdateView):
    template_name = 'generic_form.html'
    form_class = AcaoForm
    model = Acao
    success_url = 'pdic:list-acoes'

    def get_success_url(self):
        return reverse(self.success_url)

    def get_context_data(self, *args, **kwargs):
        context = super(AcaoEdit, self).get_context_data(*args, **kwargs)
        context['nome_form'] = u'Edição de ação'
        return context


class AcaoDelete(generic.edit.DeleteView):
    template_name = 'generic_delete.html'
    model = Acao
    success_url = 'pdic:list-acoes'

    def get_success_url(self):
        return reverse(self.success_url)


class Relatorio3(generic.ListView):
    template_name = 'r3.html'
    model = Acao
    context_object_name = 'acoes'

    def get_queryset(self):
        qs = super(Relatorio3, self).get_queryset()
        return qs.filter(ativa=True, tarefas__isnull=False).annotate(
            porcentagem=ExpressionWrapper(
                Sum('tarefas__porcentagem') / Count('tarefas'),
                output_field=FloatField()
            )
        ).order_by('data_inicio')


class Relatorio4(generic.DetailView):
    template_name = 'r4.html'
    model = Acao
    context_object_name = 'acao'
