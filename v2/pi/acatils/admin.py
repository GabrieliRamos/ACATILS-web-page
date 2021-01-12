from django.contrib import admin

from .models import Noticia, Mensagem


class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('autor', 'titulo', 'texto', 'criado_em')


class MensagemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'assunto', 'mensagem')


admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Mensagem, MensagemAdmin)