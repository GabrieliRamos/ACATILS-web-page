from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q

from django.template.defaultfilters import slugify

from django.views.generic import TemplateView, FormView, ListView
from django.views.generic.detail import DetailView

from .models import News, Categories
from .forms import ContactForm


class IndexView(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['news']  = News.objects.order_by('-created').all()
        return context


class NewsView(ListView):
    paginate_by = 10
    model = News
    template_name = 'news.html'


class NewsDetailView(DetailView):
    template_name='news-detail.html'
    model = News

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['related_news'] = News.objects.filter(category=context['object'].category).order_by('-created')
        return context


class ContactView(FormView):
    template_name ='contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Mensagem enviada com sucesso!')
        return super(ContactView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar mensagem! Tente novamente.')
        return super(ContactView, self).form_invalid(form, *args, **kwargs)


class CategoriesView(ListView):
    paginate_by = 10
    model = News
    template_name = 'categories.html'

    def get_queryset(self, *args, **kwargs):
        return News.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoriesView, self).get_context_data(**kwargs)
        context['category'] = Categories.objects.get(slug=self.kwargs ['slug'])
        print(self.kwargs['slug'])
        return context


class NewsSearchView(ListView):
    template_name = 'search.html'
    paginate_by = 10
    model = News

    def get_queryset(self):
        query = self.request.GET.get('search')
        results = News.objects.filter( 
                Q(title__icontains=query) |
                Q(author__icontains=query) |
                Q(text__icontains=query)
            )
        return results

    def get_context_data(self, **kwargs):
        context = super(NewsSearchView, self).get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search')
        context['news'] = self.get_queryset()
        return context