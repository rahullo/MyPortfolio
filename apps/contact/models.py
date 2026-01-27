"""
Contact app models - Contact form submissions
"""

from django.db import models
from apps.core.models import TimeStampedModel


class ContactSubmission(TimeStampedModel):
    """
    Contact form submissions
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    is_read = models.BooleanField(default=False)
    replied_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Contact Submission"
        verbose_name_plural = "Contact Submissions"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"
