from django import forms

from .models import Prompt


class PromptForm(forms.ModelForm):
    class Meta:
        model = Prompt
        fields = ("user_prompt", "gpt_key")
        labels = {
            'user_prompt': 'User Prompt',
            'gpt_key': 'GPT Key',
        }

