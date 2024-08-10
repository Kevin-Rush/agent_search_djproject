"""
This file contains the views for the core app in a Django project. It includes views for rendering templates, handling form submissions, and deleting prompts.
"""

from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import PromptForm
from .models import Prompt
from .run_research_agent import run_search


class Home(TemplateView):
    template_name = 'home.html'

def prompt_list(request):
    prompts = Prompt.objects.all()
    return render(request, "prompt_list.html", {
        "prompts": prompts
    })

def show_result(request):
    prompt = Prompt.objects.last()
    return render(request, "show_result.html", {
        "prompt": prompt
    })

def make_search(request):
    if request.method == "POST":
        form = PromptForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            search_result = run_search(form.cleaned_data['user_prompt'])
            prompt = form.save(commit=False)
            prompt.search_result = search_result
            prompt.save()
            return redirect('show_result')
    else: 
        form = PromptForm()
    return render(request, "make_search.html", {
        "form": form
    })

def delete_prompt(request, pk):
    if request.method == "POST":
        prompt = Prompt.objects.get(pk=pk)
        prompt.delete()
    return redirect('prompt_list')