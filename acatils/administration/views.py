from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import TemplateView, FormView

from core.models import News, Categories
from .forms import NewsRegisterForm


class DashboardNewsView(TemplateView):
    template_name = "dashboard-news.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardNewsView, self).get_context_data(**kwargs)
        context['news'] = News.objects.order_by('-created').all()
        return context


class NewsRegisterView(FormView):
    template_name = 'news-register.html'
    form_class = NewsRegisterForm
    success_url = reverse_lazy('dashboard-news')

    def form_valid(self, form, *args, **kwargs):
        print(form)
        form.save()
        return super(NewsRegisterView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        return super(NewsRegisterView, self).form_invalid(form, *args, **kwargs)


def search_admin(request):
    search = request.GET.get('search_admin')

    if search:
        obj = News.objects.filter(title__icontains=search)
        return render(request, 'dashboard-news.html', {'news': obj })