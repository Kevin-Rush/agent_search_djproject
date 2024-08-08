from django import forms

# from .models import Book
from .models import Prompt


# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = ('title', 'author', 'pdf', 'cover')

class PromptForm(forms.ModelForm):
    class Meta:
        model = Prompt
        fields = ("user_prompt", "gpt_key")
        labels = {
            'user_prompt': 'User Prompt',
            'gpt_key': 'GPT Key',
        }

