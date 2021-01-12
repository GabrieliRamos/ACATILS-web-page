from django.conf import settings
from django.db import models
from django.utils import timezone


class Noticia(models.Model):
    autor = models.CharField('autor', max_length=200)
    titulo = models.CharField('titulo', max_length=200)
    texto = models.TextField('texto')
    criado_em = models.DateTimeField('criado_em', default=timezone.now)

    def __str__(self):
        return self.titulo

class Mensagem(models.Model):
    nome = models.CharField('nome', max_length=100)
    email = models.EmailField('email')
    assunto = models.CharField('assunto', max_length=100)
    mensagem = models.CharField('mensagem', max_length=2000)

    def __str__(self):
        return self.assunto
