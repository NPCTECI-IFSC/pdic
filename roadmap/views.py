# encoding: utf-8
from __future__ import unicode_literals

from .forms import *
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
