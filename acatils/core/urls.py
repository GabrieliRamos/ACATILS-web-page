from django.urls import path, re_path

from django.views.generic import TemplateView

from .views import IndexView, NewsView, NewsDetailView, ContactView, CategoriesView, NewsSearchView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('quem-somos', TemplateView.as_view(template_name="about.html"), name="about"),
    path('perguntas-frequentes', TemplateView.as_view(template_name="common-questions.html"), name="common-questions"),
    path('legislacao', TemplateView.as_view(template_name="legislation.html"), name="legislation"),
    path('documentos', TemplateView.as_view(template_name="documents.html"), name='documents'),
    path('valores-de-referencia', TemplateView.as_view(template_name="reference-values.html"), name='reference-values'),
    path('seja-socio', TemplateView.as_view(template_name="associate.html"), name='associate'),

    path('contato', ContactView.as_view(), name='contact'),
    
    path('noticias', NewsView.as_view(), name='news'),
    re_path(r'^noticias/(?P<slug>[\w-]+)/$', NewsDetailView.as_view(), name='news-details'),
    re_path(r'^categorias/(?P<slug>[\w-]+)/$', CategoriesView.as_view(), name='categories'),

    path('search', NewsSearchView.as_view(), name='search')
]