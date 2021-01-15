from django.urls import path

from django.views.generic import TemplateView

from .views import DashboardNewsView, search_admin, NewsRegisterView

urlpatterns = [
    path('administracao', DashboardNewsView.as_view(), name="dashboard-news"),
    path('admin-search', search_admin, name="search_admin" ),
    path('cadastrar-noticia', NewsRegisterView.as_view(), name='news-register'),
]