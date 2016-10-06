# encoding: utf-8
from __future__ import unicode_literals

from roadmap.forms import *
from roadmap.models import *
from django.db.models import Sum, Count, ExpressionWrapper, FloatField
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views import generic


class CustomListView(generic.ListView):

    def get_queryset(self, model, filter):
        q = self.request.GET.get('q', None)
        query = model.objects.all()
        if not self.request.user.is_authenticated():
            query = query.filter(ativa=True)
        if q:
            query = query.filter(**{filter: q})
        return query


class CustomFormView(generic.FormView):

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(CustomFormView, self).form_valid(form)


class CustomDeleteView(generic.edit.DeleteView):

    def get_success_url(self):
        return reverse(self.success_url)

    def post(self, request, *args, **kwargs):
        obj = self.model.objects.get(id=self.kwargs.get('pk'))
        obj.ativa = False
        obj.save()
        return redirect(self.get_success_url())


class Index(generic.TemplateView):
    template_name = 'index.html'


class TarefaList(CustomListView):
    template_name = 'tarefa_list.html'
    context_object_name = 'tarefas'
    model = Tarefa
    paginate_by = 15

    def get_queryset(self):
        filter = 'descricao__icontains'
        return super(TarefaList, self).get_queryset(Tarefa, filter)


class TarefaDetail(generic.DetailView):
    template_name = 'tarefa_detail.html'
    context_object_name = 'tarefa'
    model = Tarefa


class TarefaCreate(CustomFormView):
    template_name = 'tarefa_form.html'
    form_class = TarefaForm
    success_url = 'pdic:list-tarefas'

    def get_initial(self):
        initial = super(TarefaCreate, self).get_initial()
        initial['responsavel'] = self.request.user
        return initial

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


class TarefaDelete(CustomDeleteView):
    template_name = 'generic_delete.html'
    model = Tarefa
    success_url = 'pdic:list-tarefas'


class RotaList(CustomListView):
    template_name = 'rota_list.html'
    context_object_name = 'rotas'
    model = Rota
    paginate_by = 15

    def get_queryset(self):
        filter = 'nome__icontains'
        return super(RotaList, self).get_queryset(Rota, filter)


class RotaCreate(CustomFormView):
    template_name = 'generic_form.html'
    form_class = RotaForm
    success_url = 'pdic:list-rotas'

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


class RotaDelete(CustomDeleteView):
    template_name = 'generic_delete.html'
    model = Rota
    success_url = 'pdic:list-rotas'


class VisaoList(CustomListView):
    template_name = 'visao_list.html'
    context_object_name = 'visoes'
    model = Visao
    paginate_by = 15

    def get_queryset(self):
        filter = 'descricao__icontains'
        return super(VisaoList, self).get_queryset(Visao, filter)


class VisaoCreate(CustomFormView):
    template_name = 'generic_form.html'
    form_class = VisaoForm
    success_url = 'pdic:list-visoes'

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


class VisaoDelete(CustomDeleteView):
    template_name = 'generic_delete.html'
    model = Visao
    success_url = 'pdic:list-visoes'


class FatorList(CustomListView):
    template_name = 'fator_list.html'
    context_object_name = 'fatores'
    model = Fator
    paginate_by = 15

    def get_queryset(self):
        filter = 'nome__icontains'
        return super(FatorList, self).get_queryset(Fator, filter)


class FatorCreate(CustomFormView):
    template_name = 'generic_form.html'
    form_class = FatorForm
    success_url = 'pdic:list-fatores'

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


class FatorDelete(CustomDeleteView):
    template_name = 'generic_delete.html'
    model = Fator
    success_url = 'pdic:list-fatores'


class TemaList(CustomListView):
    template_name = 'tema_list.html'
    context_object_name = 'temas'
    model = Tema
    paginate_by = 15

    def get_queryset(self):
        filter = 'descricao__icontains'
        return super(TemaList, self).get_queryset(Tema, filter)


class TemaCreate(CustomFormView):
    template_name = 'generic_form.html'
    form_class = TemaForm
    success_url = 'pdic:list-temas'

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


class TemaDelete(CustomDeleteView):
    template_name = 'generic_delete.html'
    model = Tema
    success_url = 'pdic:list-temas'


class AcaoList(CustomListView):
    template_name = 'acao_list.html'
    context_object_name = 'acoes'
    model = Acao
    paginate_by = 10

    def get_queryset(self):
        filter = 'descricao__icontains'
        return super(AcaoList, self).get_queryset(Acao, filter)


class AcaoDetail(generic.DetailView):
    template_name = 'acao_detail.html'
    context_object_name = 'acao'
    model = Acao


class AcaoCreate(CustomFormView):
    template_name = 'generic_form.html'
    form_class = AcaoForm
    success_url = 'pdic:list-acoes'

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


class TendenciaList(CustomListView):
    template_name = 'tendencia_list.html'
    context_object_name = 'tendencias'
    model = Tendencia
    paginate_by = 10

    def get_queryset(self):
        filter = 'descricao__icontains'
        return super(TendenciaList, self).get_queryset(Tendencia, filter)


class TendenciaCreate(CustomFormView):
    template_name = 'generic_form.html'
    form_class = TendenciaForm
    success_url = 'pdic:list-tendencias'

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


class ConhecimentoList(CustomListView):
    template_name = 'conhecimento_list.html'
    context_object_name = 'conhecimentos'
    model = Conhecimento
    paginate_by = 10

    def get_queryset(self):
        filter = 'descricao__icontains'
        return super(ConhecimentoList, self).get_queryset(Conhecimento, filter)


class ConhecimentoCreate(CustomFormView):
    template_name = 'conhecimento_form.html'
    form_class = ConhecimentoForm
    success_url = 'pdic:list-conhecimentos'

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
