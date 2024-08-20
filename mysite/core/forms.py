"""
This file defines a Django form called PromptForm, which is used to create a form for the Prompt model. The form includes fields for the user prompt, the GPT key, and the search results.
"""
from django import forms

from .models import Prompt
from .models import Document

class PromptForm(forms.ModelForm):
    class Meta:
        model = Prompt
        fields = ("user_prompt", "gpt_key", "search_result")
        
        labels = {
            'user_prompt': 'User Prompt',
            'gpt_key': 'GPT Key',
            'search_result': 'Search Result',
        }

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['user_prompt', 'doc_type']
        
        labels = {
            'user_prompt': 'User Prompt',
            'doc_type': 'Document Type',
        }
        
        widgets = {
            'user_prompt': forms.TextInput(attrs={'class': 'form-control'}),
            'doc_type': forms.Select(attrs={'class': 'form-control'}),
        }
