"""
Projects app admin configuration
"""

from django.contrib import admin
from .models import Project, ProjectImage, ProjectFeature


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ['image', 'caption', 'order']


class ProjectFeatureInline(admin.TabularInline):
    model = ProjectFeature
    extra = 1
    fields = ['feature', 'order']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'start_date', 'end_date', 'is_featured', 'order']
    list_filter = ['category', 'is_featured', 'start_date']
    list_editable = ['is_featured', 'order']
    search_fields = ['title', 'short_description', 'detailed_description']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    inlines = [ProjectFeatureInline, ProjectImageInline]
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'category', 'short_description')
        }),
        ('Details', {
            'fields': ('detailed_description', 'tech_stack')
        }),
        ('Timeline', {
            'fields': ('start_date', 'end_date')
        }),
        ('Links & Media', {
            'fields': ('github_url', 'live_url', 'featured_image')
        }),
        ('Display Options', {
            'fields': ('is_featured', 'order')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
