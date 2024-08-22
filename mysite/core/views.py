"""
im testing the git iOS app for coding from my phone
"""

"""
This file contains the views for the core app in a Django project. It includes views for rendering templates, handling form submissions, and deleting prompts.
"""

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

import markdown

from .forms import PromptForm
from .models import Prompt
from .forms import DocumentForm
from .models import Document

from .run_research_agent import run_search




class Home(TemplateView):
    template_name = 'home.html'

#all admin views

def contact_info(request):    
    return render(request, "contact_info.html")

#all the views for the search functionality

def search_landing(request):    
    return render(request, "search_landing.html")

def prompt_list(request):
    prompts = Prompt.objects.all().order_by('-created_at')
    
    return render(request, "prompt_list.html", {
        "prompts": prompts
    })

def show_result(request, prompt_id):
    prompt = get_object_or_404(Prompt, id=prompt_id)
    return render(request, "show_result.html", {
        "prompt": prompt
    })

def make_search(request):
    if request.method == "POST":
        form = PromptForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            results_markdown = run_search(form.cleaned_data['user_prompt'])
            results_html = markdown.markdown(results_markdown)
            prompt = form.save(commit=False)
            prompt.search_result = results_html
            prompt.save()
            # return redirect('show_result')
            return redirect('show_result', prompt_id=prompt.id)
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

#all the views for the document creation

def gen_biz_docs(request):
    return render(request, "gen_biz_docs.html")

def create_document(request):
    if request.method == "POST":
        form = DocumentForm(request.POST)
        if form.is_valid():
            user_prompt = form.cleaned_data['user_prompt']
            doc_type = form.cleaned_data['doc_type']
            
            search_result_markdown = run_search(user_prompt)  
            search_result_html = markdown.markdown(search_result_markdown)
            
            document = form.save(commit=False)
            document.search_result = search_result_html
            document.save()
            
            return redirect('document_success')  
    else:
        form = DocumentForm()

    return render(request, "create_document.html", {"form": form})

#all the views for the ppxt support

def ppxt_support(request):
    return render(request, "ppxt_support.html")
