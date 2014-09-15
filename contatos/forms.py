#!/usr/bin/python
#  -*- coding: utf-8 -*-
from django import forms
from django.forms import fields
from django.core.exceptions import ValidationError
from models import Contato

YES_OR_NO = [('SIM','NÃO'),('True','False')]

class ContatoCadastroForm(forms.ModelForm):
    """
    Formulário de cadastro de Contatos
    """
    class Meta:
        model = Contato
        fields = ('nome', 'email', 'senha', 'telefone', 'cpf', 'data_nascimento', 'ativo')

    def clean_nome(self):
        return self.cleaned_data['nome']

    def __init__(self, *args, **kwargs):
        self.base_fields['nome'].widget = forms.TextInput(attrs={'size': '40'})
        self.base_fields['nome'].widget.attrs['class'] = 'form-control'
        self.base_fields['nome'].widget.attrs['placeholder'] = 'obrigatório'

        self.base_fields['email'].widget = forms.TextInput()
        self.base_fields['email'].widget.attrs['class'] = 'form-control'
        
        self.base_fields['senha'].widget = forms.PasswordInput()
        self.base_fields['senha'].widget.attrs['class'] = 'form-control'

        self.base_fields['telefone'].widget = forms.TextInput()
        self.base_fields['telefone'].widget.attrs['class'] = 'form-control'
        
        self.base_fields['cpf'].widget = forms.TextInput()
        self.base_fields['cpf'].widget.attrs['class'] = 'form-control'
        
        self.base_fields['data_nascimento'].widget = forms.DateInput()
        self.base_fields['data_nascimento'].tamanho = 2
        self.base_fields['data_nascimento'].widget.attrs['class'] = 'form-control'

        super(ContatoCadastroForm, self).__init__(*args, **kwargs)


class ContatoEditarForm(ContatoCadastroForm):
    """
    Formulário de editar Contatos
    """

    def __init__(self, *args, **kwargs):
        self.base_fields['nome'].widget = forms.TextInput(attrs={'size': '40'})
        self.base_fields['nome'].widget.attrs['class'] = 'form-control'
        self.base_fields['nome'].widget.attrs['placeholder'] = 'obrigatório'

        self.base_fields['email'].widget = forms.TextInput()
        self.base_fields['email'].widget.attrs['class'] = 'form-control'

        self.base_fields['senha'].widget = forms.PasswordInput()
        self.base_fields['senha'].widget.attrs['class'] = 'form-control'

        self.base_fields['telefone'].widget = forms.TextInput()
        self.base_fields['telefone'].widget.attrs['class'] = 'form-control'
        
        self.base_fields['cpf'].widget = forms.TextInput()
        self.base_fields['cpf'].widget.attrs['class'] = 'form-control'
        
        self.base_fields['data_nascimento'].widget = forms.DateInput()
        self.base_fields['data_nascimento'].tamanho = 2
        self.base_fields['data_nascimento'].widget.attrs['class'] = 'form-control'
        
        super(ContatoCadastroForm, self).__init__(*args, **kwargs)