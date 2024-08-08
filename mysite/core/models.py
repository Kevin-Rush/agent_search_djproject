"""
Models for the core app in the Django project. Includes the Prompt model for storing user prompts and related information.
"""

from django.db import models

class Prompt(models.Model):
    user_prompt = models.CharField(max_length=256)
    gpt_key = models.CharField(max_length=56)
    search_result = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user_prompt
    
    
    # def delete(self, *args, **kwargs):
    #     self.gpt_key.delete()
    #     self.prompt.delete()
    #     super().delete(*args, **kwargs)