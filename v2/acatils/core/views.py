from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView, FormView

from .models import News
from .forms import ContactForm

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


class ContactView(FormView):
    template_name ='contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Mensagem enviada com sucesso!')
        return super(ContactView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar!')
        return super(ContactView, self).form_invalid(form, *args, **kwargs)
