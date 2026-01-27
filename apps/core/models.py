"""
Core models - Base abstract models for reusability
"""

from django.db import models


class TimeStampedModel(models.Model):
    """
    Abstract base model with created and updated timestamps
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SEOModel(models.Model):
    """
    Abstract base model for SEO fields
    """
    meta_title = models.CharField(max_length=200, blank=True, help_text="SEO title")
    meta_description = models.TextField(max_length=300, blank=True, help_text="SEO description")

    class Meta:
        abstract = True
