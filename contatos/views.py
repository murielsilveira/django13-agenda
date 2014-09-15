#!/usr/bin/python
#  -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect

from contatos.models import Contato
from contatos.forms import ContatoCadastroForm, ContatoEditarForm

def contatos_listar(request):
    contatos = Contato.objects.all()
    return render_to_response('contatos/listar.html', {"contatos": contatos}, context_instance=RequestContext(request))


def contatos_cadastrar(request):
    """
    Cadastro de contatos
    """
    if request.method == 'POST':
        form = ContatoCadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(contatos_listar)
    else:
        form = ContatoCadastroForm()

    return render_to_response('contatos/cadastrar.html', {'form': form}, context_instance=RequestContext(request))


def contatos_editar(request, contato_id):
    """
    Edição de contatos
    """
    contato = get_object_or_404(Contato, id=contato_id)

    if request.method == 'POST':
        form = ContatoEditarForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            return redirect(contatos_listar)
    else:
        form = ContatoEditarForm(instance=contato)

    return render_to_response('contatos/editar.html', {'form': form}, context_instance=RequestContext(request))


def contatos_excluir(request, contato_id):
    """
    Exclusão de contatos
    """
    return redirect(contatos_listar)