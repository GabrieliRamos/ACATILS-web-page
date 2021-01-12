from django.urls import path
from .views import index, contato, documentos, legislacao, perguntasfrequentes, quemsomos, cadastrarNoticia, valoresdereferencia, noticias, noticia, login, adminNoticias, mensagens, editarNoticia

urlpatterns = [
    path('', index, name="index"),
    path('contato', contato, name="contato"),
    path('documentos', documentos, name="documentos"),
    path('legislacao', legislacao, name="legislacao"),
    path('perguntasfrequentes', perguntasfrequentes, name="perguntasfrequentes"),
    path('quemsomos', quemsomos, name="quemsomos"),
    path('valoresdereferencia', valoresdereferencia, name="valoresdereferencia"),
    path('noticias', noticias, name="noticias"),
    path('noticia/<int:pk>', noticia, name="noticia"),
    path('login', login, name="login"),
    path('mensagens', mensagens, name="mensagens"),
    path('admin/noticias', adminNoticias, name="admin-noticias"),
    path('editar-noticia/<int:pk>', editarNoticia, name="editar-noticia"),
    path('cadastrar_noticia', cadastrarNoticia, name="cadastrar_noticia")
]