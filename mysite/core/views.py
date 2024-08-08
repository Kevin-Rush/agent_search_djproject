from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView

from .forms import PromptForm
from .models import Prompt

class Home(TemplateView):
    template_name = 'home.html'

def prompt_list(request):
    prompts = Prompt.objects.all()
    return render(request, "prompt_list.html", {
        "prompts": prompts
    })

def make_search(request):
    if request.method == "POST":
        form = PromptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prompt_list')
            # What do I want to do after I save the form? Do I need to reroute them? I think I should do the entire search on this page.
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