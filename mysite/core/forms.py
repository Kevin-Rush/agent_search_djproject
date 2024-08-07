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
        field = ("prompt_string", "gpt_key")

