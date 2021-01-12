from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import Noticia, Mensagem
from .forms import ContatoForm, NoticiaForm


def index(request):
    return render(request, 'index.html')


def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            nova_msg = Mensagem(nome=nome, email=email, assunto=assunto, mensagem=mensagem)
            nova_msg.save()

            messages.success(request, 'Enviado com sucesso! ')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao submeter o formulário :(')

    return render(request, 'contato.html', {'form': form})


def documentos(request):
    return render(request, 'documentos.html')


def legislacao(request):
    return render(request, 'legislacao.html')


def perguntasfrequentes(request):
    return render(request, 'perguntasfrequentes.html')


def quemsomos(request):
    return render(request, 'quemsomos.html')


def valoresdereferencia(request):
    return render(request, 'valoresdereferencia.html')


def noticias(request):
    noti = Noticia.objects.all()
    return render(request, 'noticias.html', {'noticias': noti})


def noticia(request, pk):
    noti = Noticia.objects.get(id=pk)

    return render(request, 'noticia.html', {'noticia': noti})


def login(request):
    return render(request, 'login.html')


def mensagens(request):
    msgs = Mensagem.objects.all()
    return render(request, 'msg.html', {'mensagens': msgs})


def adminNoticias(request):
    noti = Noticia.objects.all()
    return render(request, 'admin-noticias.html', {'noticias': noti})


def editarNoticia(request, pk):
    noticia = Noticia.objects.get(id=pk)
    form = NoticiaForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            noticia.titulo = form.cleaned_data['titulo']
            noticia.autor = form.cleaned_data['autor']
            noticia.texto = form.cleaned_data['texto']

            noticia.save()

            messages.success(request, 'Enviado com sucesso! ')
            form = NoticiaForm()

    return render(request, 'editar-noticia.html', {'noticia': noticia})


def cadastrarNoticia(request):
    form = NoticiaForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            autor = form.cleaned_data['autor']
            texto = form.cleaned_data['texto']

            print(titulo, autor, texto)

            nova_noticia = Noticia(titulo=titulo, autor=autor, texto=texto)
            nova_noticia.save()

            messages.success(request, 'Enviado com sucesso! ')
            form = NoticiaForm()
        else:
            messages.error(request, 'Erro ao submeter o formulário :(')

    return render(request, 'cadastrar-noticia.html')

