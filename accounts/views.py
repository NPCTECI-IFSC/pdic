# encoding: utf-8
from accounts.forms import UsuarioForm
from django.views import generic


class UsuarioForm(generic.FormView):
    template_name = 'usuario_form.html'
    form_class = UsuarioForm
    success_url = 'index'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(UsuarioForm, self).form_valid(form)
