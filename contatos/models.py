from django.db import models


class Contato(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=200)
    email = models.EmailField(verbose_name='E-mail', max_length=200)
    senha = models.CharField(verbose_name='Senha', max_length=10)
    telefone = models.CharField(verbose_name='Telefone', blank=True, max_length=15)
    cpf = models.BigIntegerField(verbose_name='CPF', max_length=11)
    data_nascimento = models.DateField(verbose_name='Data de Nascimento', auto_now_add=False)
    ativo = models.BooleanField(verbose_name='Ativo', default=True)

    def __unicode__(self):
        return "".join(self.nome, ' - ', self.email)