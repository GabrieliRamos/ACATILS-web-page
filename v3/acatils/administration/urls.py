from django.urls import path

from django.views.generic import TemplateView

urlpatterns = [
    path('administracao', TemplateView.as_view(template_name="base-admin.html")),
]