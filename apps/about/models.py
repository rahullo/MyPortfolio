"""
About app models - Profile information
"""

from django.db import models
from apps.core.models import TimeStampedModel, SEOModel


class Profile(TimeStampedModel, SEOModel):
    """
    Professional profile model
    """
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=200, help_text="Professional role/title")
    email = models.EmailField()
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    summary = models.TextField(help_text="Professional summary/bio")
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume_file = models.FileField(upload_to='resume/', blank=True, null=True)
    is_active = models.BooleanField(default=True, help_text="Only one profile should be active")

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ['-is_active', '-created_at']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Ensure only one active profile
        if self.is_active:
            Profile.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)
