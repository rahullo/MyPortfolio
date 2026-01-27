"""
Skills app views
"""

from django.shortcuts import render
from .models import SkillCategory


def skills(request):
    """
    Skills page view
    """
    context = {
        'skill_categories': SkillCategory.objects.prefetch_related('skills').all(),
    }
    return render(request, 'skills/skills.html', context)
