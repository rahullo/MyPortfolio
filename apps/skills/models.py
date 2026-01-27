"""
Skills app models - Technical skills categorization
"""

from django.db import models


class SkillCategory(models.Model):
    """
    Categories for organizing skills
    """
    name = models.CharField(max_length=100, help_text="e.g., Programming Languages, Frameworks")
    icon = models.CharField(max_length=50, blank=True, help_text="Font Awesome icon class")
    order = models.IntegerField(default=0, help_text="Display order")

    class Meta:
        verbose_name = "Skill Category"
        verbose_name_plural = "Skill Categories"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Skill(models.Model):
    """
    Individual skills within categories
    """
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(default=50, help_text="Proficiency level 1-100")
    icon = models.CharField(max_length=50, blank=True, help_text="Font Awesome icon class")
    order = models.IntegerField(default=0, help_text="Display order within category")

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.category.name})"
