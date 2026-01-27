"""
Education app admin configuration
"""

from django.contrib import admin
from .models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'cgpa', 'max_cgpa', 'start_date', 'end_date', 'order']
    list_filter = ['start_date', 'institution']
    list_editable = ['order']
    search_fields = ['degree', 'field', 'institution']
    fieldsets = (
        ('Degree Information', {
            'fields': ('degree', 'field', 'institution', 'location')
        }),
        ('Academic Performance', {
            'fields': ('cgpa', 'max_cgpa')
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date')
        }),
        ('Display', {
            'fields': ('order',)
        }),
    )
