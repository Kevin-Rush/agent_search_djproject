# from typing import Any
from django.db import models


# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=100)
#     pdf = models.FileField(upload_to='books/pdfs/')
#     cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

#     def __str__(self):
#         return self.title

#     def delete(self, *args, **kwargs):
#         self.pdf.delete()
#         self.cover.delete()
#         super().delete(*args, **kwargs)

class Prompt(models.Model):
    user_prompt = models.CharField(max_length=256)
    gpt_key = models.CharField(max_length=56)

    def __str__(self):
        return self.user_prompt
    
    # def delete(self, *args, **kwargs):
    #     self.gpt_key.delete()
    #     self.prompt.delete()
    #     super().delete(*args, **kwargs)