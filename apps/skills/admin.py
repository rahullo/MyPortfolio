"""
Skills app admin configuration
"""

from django.contrib import admin
from .models import SkillCategory, Skill


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ['name', 'proficiency', 'icon', 'order']


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'skill_count']
    list_editable = ['order']
    search_fields = ['name']
    inlines = [SkillInline]

    def skill_count(self, obj):
        return obj.skills.count()
    skill_count.short_description = 'Number of Skills'


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_filter = ['category']
    list_editable = ['proficiency', 'order']
    search_fields = ['name']
