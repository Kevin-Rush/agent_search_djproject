from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView

from .forms import PromptForm

class Home(TemplateView):
    template_name = 'home.html'


def make_search(request):
    return render(request, "make_search.html")