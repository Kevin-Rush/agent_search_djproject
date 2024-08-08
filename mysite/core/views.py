from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView

from .forms import PromptForm

class Home(TemplateView):
    template_name = 'home.html'

def prompt_list(request):
    return render(request, "prompt_list.html")

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