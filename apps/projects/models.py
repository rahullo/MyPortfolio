"""
Projects app models - Portfolio projects
"""

from django.db import models
from django.utils.text import slugify
from apps.core.models import TimeStampedModel, SEOModel


class Project(TimeStampedModel, SEOModel):
    """
    Portfolio project model
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    short_description = models.TextField(max_length=300, help_text="Brief project summary")
    detailed_description = models.TextField(help_text="Full project description")
    tech_stack = models.TextField(help_text="Technologies used (comma-separated)")
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    featured_image = models.ImageField(upload_to='projects/', blank=True, null=True)
    is_featured = models.BooleanField(default=False, help_text="Show on homepage")
    
    PROJECT_CATEGORIES = (
        ('standard', 'Personal Project'),
        ('freelance', 'Freelance Project'),
    )
    category = models.CharField(max_length=20, choices=PROJECT_CATEGORIES, default='standard')
    
    order = models.IntegerField(default=0, help_text="Display order")

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['order', '-start_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_tech_stack_list(self):
        """Return tech stack as a list"""
        return [tech.strip() for tech in self.tech_stack.split(',') if tech.strip()]


class ProjectImage(models.Model):
    """
    Additional images for a project
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Project Image"
        verbose_name_plural = "Project Images"
        ordering = ['order']

    def __str__(self):
        return f"{self.project.title} - Image {self.order}"


class ProjectFeature(models.Model):
    """
    Key features of a project
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='features')
    feature = models.TextField(help_text="Feature description")
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Project Feature"
        verbose_name_plural = "Project Features"
        ordering = ['order']

    def __str__(self):
        return f"{self.project.title} - Feature {self.order}"
