from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils import timezone
from django.template.defaultfilters import slugify

from django.views.generic import TemplateView, FormView

from .models import News, Categories
from .forms import ContactForm

class IndexView(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['news'] = News.objects.order_by('-created').all()
        return context


class NewsView(TemplateView):
    template_name = 'news.html'

    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        context['news'] = News.objects.order_by('-created').all()
        return context


class NewsDetailView(TemplateView):
    template_name = 'news-detail.html'

    def get_context_data(self, slug, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['news'] = News.objects.get(slug=slug)
        context['related_news'] = News.objects.filter(category=context['news'].category).order_by('-created')
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


class CategoriesView(TemplateView):
    template_name = 'categories.html'

    def get_context_data(self, slug, **kwargs):
        context = super(CategoriesView, self).get_context_data(**kwargs)
        context['category'] = Categories.objects.get(slug=slug)
        context['news'] = News.objects.filter(category__slug=slug).order_by('-created')
        return context


def search(request):
    search = request.GET.get('search')

    if search:
        obj = News.objects.filter(title__icontains=search)
        return render(request, 'search.html', {'news': obj, 'search': search })
    else:
        return render(request, 'index.html')
        


    

