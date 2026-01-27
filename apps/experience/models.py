"""
Experience app models - Professional work experience
"""

from django.db import models
from apps.core.models import TimeStampedModel


class Experience(TimeStampedModel):
    """
    Professional work experience
    """
    title = models.CharField(max_length=200, help_text="Job title")
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text="Leave blank if current")
    is_current = models.BooleanField(default=False)
    description = models.TextField(help_text="Overall role description")
    order = models.IntegerField(default=0, help_text="Display order (0 = most recent)")

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"
        ordering = ['order', '-start_date']

    def __str__(self):
        return f"{self.title} at {self.company}"


class ExperienceHighlight(models.Model):
    """
    Key achievements/responsibilities for an experience
    """
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='highlights')
    text = models.TextField(help_text="Achievement or responsibility")
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Experience Highlight"
        verbose_name_plural = "Experience Highlights"
        ordering = ['order']

    def __str__(self):
        return f"{self.experience.title} - Highlight {self.order}"


class ExperienceTechnology(models.Model):
    """
    Technologies used in an experience
    """
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='technologies')
    technology = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Experience Technology"
        verbose_name_plural = "Experience Technologies"
        ordering = ['technology']

    def __str__(self):
        return f"{self.experience.title} - {self.technology}"
