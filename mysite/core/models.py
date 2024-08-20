"""
Models for the core app in the Django project. Includes the Prompt model for storing user prompts and related information.
"""

from django.db import models

class Prompt(models.Model):
    user_prompt = models.CharField(max_length=256)
    gpt_key = models.CharField(max_length=56)
    search_result = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_prompt

class Document(models.Model):
    DOC_TYPES = [
        ('pptx', 'PowerPoint'),
    ]
    
    user_prompt = models.CharField(max_length=256)
    doc_type = models.CharField(max_length=50, choices=DOC_TYPES)
    search_result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.doc_type.capitalize()} created on {self.created_at.strftime('%Y-%m-%d')}"


