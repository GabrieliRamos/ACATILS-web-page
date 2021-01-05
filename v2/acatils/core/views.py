from django.shortcuts import render
from django.views.generic import FormView

class IndexView(FormView):
    template_name = 'index.html'
