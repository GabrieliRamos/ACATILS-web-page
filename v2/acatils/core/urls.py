from django.urls import path

from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('quem-somos', TemplateView.as_view(template_name="about.html"), name="about"),
    path('perguntas-frequentes', TemplateView.as_view(template_name="common-questions.html"), name="common-questions"),
    path('legislacao', TemplateView.as_view(template_name="legislation.html"), name="legislation"),
    path('documentos', TemplateView.as_view(template_name="documents.html"), name='documents'),
    path('valores-de-referencia', TemplateView.as_view(template_name="reference-values.html"), name='reference-values'),

    path('contato', TemplateView.as_view(template_name="contact.html"), name='contact'),
    path('noticias', TemplateView.as_view(template_name="news.html"), name='news'),
]