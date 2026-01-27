"""
Experience app admin configuration
"""

from django.contrib import admin
from .models import Experience, ExperienceHighlight, ExperienceTechnology


class ExperienceHighlightInline(admin.TabularInline):
    model = ExperienceHighlight
    extra = 1
    fields = ['text', 'order']


class ExperienceTechnologyInline(admin.TabularInline):
    model = ExperienceTechnology
    extra = 1
    fields = ['technology']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'location', 'start_date', 'end_date', 'is_current', 'order']
    list_filter = ['is_current', 'start_date']
    list_editable = ['order']
    search_fields = ['title', 'company', 'description']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [ExperienceHighlightInline, ExperienceTechnologyInline]
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'company', 'location')
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        ('Details', {
            'fields': ('description', 'order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
