# encoding: utf-8
from __future__ import unicode_literals

from roadmap.forms import *
from roadmap.models import *
from django.db.models import Sum, Count, ExpressionWrapper, FloatField
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
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


class TarefaDetail(generic.DetailView):
    template_name = 'tarefa_detail.html'
    context_object_name = 'tarefa'
    model = Tarefa


class TarefaCreate(generic.FormView):
    template_name = 'tarefa_form.html'
    form_class = TarefaForm
    success_url = 'pdic:list-tarefas'

    def get_success_url(self):
        return reverse(self.success_url)

    def get_initial(self):
        initial = super(TarefaCreate, self).get_initial()
        initial['responsavel'] = self.request.user
        return initial

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

    def post(self, request, *args, **kwargs):
        tarefa = Tarefa.objects.get(id=self.kwargs.get('pk'))
        tarefa.ativa = False
        tarefa.save()
        return redirect(self.get_success_url())


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

    def post(self, request, *args, **kwargs):
        rota = Rota.objects.get(id=self.kwargs.get('pk'))
        rota.ativa = False
        rota.save()
        return redirect(self.get_success_url())


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

    def post(self, request, *args, **kwargs):
        visao = Visao.objects.get(id=self.kwargs.get('pk'))
        visao.ativa = False
        visao.save()
        return redirect(self.get_success_url())


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

    def post(self, request, *args, **kwargs):
        fator = Fator.objects.get(id=self.kwargs.get('pk'))
        fator.ativa = False
        fator.save()
        return redirect(self.get_success_url())


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

    def post(self, request, *args, **kwargs):
        tema = Tema.objects.get(id=self.kwargs.get('pk'))
        tema.ativa = False
        tema.save()
        return redirect(self.get_success_url())


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


class AcaoDetail(generic.DetailView):
    template_name = 'acao_detail.html'
    context_object_name = 'acao'
    model = Acao


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

    def post(self, request, *args, **kwargs):
        acao = Acao.objects.get(id=self.kwargs.get('pk'))
        acao.ativa = False
        acao.save()
        return redirect(self.get_success_url())


class TendenciaList(generic.ListView):
    template_name = 'tendencia_list.html'
    context_object_name = 'tendencias'
    model = Tendencia
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        query = Tendencia.objects.all()
        if not self.request.user.is_authenticated():
            query = query.filter(ativa=True)
        if q:
            query = query.filter(descricao__icontains=q)
        return query


class TendenciaCreate(generic.FormView):
    template_name = 'generic_form.html'
    form_class = TendenciaForm
    success_url = 'pdic:list-tendencias'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(TendenciaCreate, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(TendenciaCreate, self).get_context_data(*args, **kwargs)
        context['nome_form'] = u'Cadastro de tendência setorial'
        return context


class TendenciaEdit(generic.edit.UpdateView):
    template_name = 'generic_form.html'
    form_class = TendenciaForm
    model = Tendencia
    success_url = 'pdic:list-tendencias'

    def get_success_url(self):
        return reverse(self.success_url)

    def get_context_data(self, *args, **kwargs):
        context = super(TendenciaEdit, self).get_context_data(*args, **kwargs)
        context['nome_form'] = u'Edição de tendência setorial'
        return context


class TendenciaDelete(generic.edit.DeleteView):
    template_name = 'generic_delete.html'
    model = Tendencia
    success_url = 'pdic:list-tendencias'

    def get_success_url(self):
        return reverse(self.success_url)

    def post(self, request, *args, **kwargs):
        tendencia = Tendencia.objects.get(id=self.kwargs.get('pk'))
        tendencia.ativa = False
        tendencia.save()
        return redirect(self.get_success_url())


class ConhecimentoList(generic.ListView):
    template_name = 'conhecimento_list.html'
    context_object_name = 'conhecimentos'
    model = Conhecimento
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        query = Conhecimento.objects.all()
        if not self.request.user.is_authenticated():
            query = query.filter(ativa=True)
        if q:
            query = query.filter(descricao__icontains=q)
        return query


class ConhecimentoCreate(generic.FormView):
    template_name = 'conhecimento_form.html'
    form_class = ConhecimentoForm
    success_url = 'pdic:list-conhecimentos'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(ConhecimentoCreate, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ConhecimentoCreate, self).get_context_data(*args, **kwargs)
        context['nome_form'] = u'Cadastro de conhecimento chave'
        return context


class ConhecimentoEdit(generic.edit.UpdateView):
    template_name = 'conhecimento_form.html'
    form_class = ConhecimentoForm
    model = Conhecimento
    success_url = 'pdic:list-conhecimentos'

    def get_success_url(self):
        return reverse(self.success_url)

    def get_context_data(self, *args, **kwargs):
        context = super(ConhecimentoEdit, self).get_context_data(*args, **kwargs)
        context['nome_form'] = u'Edição de conhecimento chave'
        return context


class ConhecimentoDelete(generic.edit.DeleteView):
    template_name = 'generic_delete.html'
    model = Conhecimento
    success_url = 'pdic:list-conhecimentos'

    def get_success_url(self):
        return reverse(self.success_url)

    def post(self, request, *args, **kwargs):
        conhecimento = Conhecimento.objects.get(id=self.kwargs.get('pk'))
        conhecimento.ativa = False
        conhecimento.save()
        return redirect(self.get_success_url())


class Relatorio1(generic.ListView):
    template_name = 'r1.html'
    model = Rota
    context_object_name = 'rotas'


class Relatorio2(generic.TemplateView):
    template_name = 'r2.html'


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


class CustomGraph(generic.TemplateView):
    template_name = 'custom_graph.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CustomGraph, self).get_context_data(*args, **kwargs)
        context['type'] = self.request.GET.get('type')
        return context
