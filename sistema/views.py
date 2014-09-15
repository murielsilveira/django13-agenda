#!/usr/bin/python
#  -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect


def sistema(request):
    """
    Define para onde o usuário será encaminhado
    """
    #logado = True
    #if logado:
    #return redirect(login)
    return redirect(menu)


def menu(request):
    """
    Exibe o menu do sistema, a página principal
    """
    return render_to_response('sistema/logado.html', context_instance=RequestContext(request))


def login(request):
    """
    Exibe a tela de login do sistema
    """
    return render_to_response('sistema/login.html', context_instance=RequestContext(request))
