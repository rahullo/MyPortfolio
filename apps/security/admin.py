"""
Security app admin configuration
"""

from django.contrib import admin
from .models import SecurityFeature


@admin.register(SecurityFeature)
class SecurityFeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'order']
    list_filter = ['category']
    list_editable = ['order']
    search_fields = ['title', 'description']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'category', 'icon')
        }),
        ('Details', {
            'fields': ('description', 'order')
        }),
    )
