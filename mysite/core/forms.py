"""
This file defines a Django form called PromptForm, which is used to create a form for the Prompt model. The form includes fields for the user prompt, the GPT key, and the search results.
"""
from django import forms

from .models import Prompt

class PromptForm(forms.ModelForm):
    class Meta:
        model = Prompt
        fields = ("user_prompt", "gpt_key", "search_result")
        
        labels = {
            'user_prompt': 'User Prompt',
            'gpt_key': 'GPT Key',
            'search_result': 'Search Result',
        }
    
    # def __init__(self, *args, **kwargs):
    #     super(PromptForm, self).__init__(*args, **kwargs)
    #     self.fields['search_result'].initial = ''

    


