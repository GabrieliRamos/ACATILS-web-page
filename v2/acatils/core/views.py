from django.shortcuts import render
from django.views.generic import TemplateView

from .models import News

class IndexView(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['news'] = News.objects.order_by('created').all()
        return context

class NewsView(TemplateView):
    template_name = 'news.html'

    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        context['news'] = News.objects.order_by('created').all()
        return context

class NewsDetailView(TemplateView):
    template_name = 'news-detail.html'

    def get_context_data(self, slug, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['news'] = News.objects.order_by('created').get(slug=slug)
        return context

