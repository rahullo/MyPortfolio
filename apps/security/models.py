"""
Security app models - Security features showcase
"""

from django.db import models


class SecurityFeature(models.Model):
    """
    Security implementations and practices
    """
    CATEGORY_CHOICES = [
        ('authentication', 'Authentication'),
        ('api_security', 'API Security'),
        ('data_protection', 'Data Protection'),
        ('infrastructure', 'Infrastructure Security'),
        ('compliance', 'Compliance & Standards'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(help_text="Detailed description of the security feature")
    icon = models.CharField(max_length=50, blank=True, help_text="Font Awesome icon class")
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Security Feature"
        verbose_name_plural = "Security Features"
        ordering = ['order', 'category', 'title']

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"
