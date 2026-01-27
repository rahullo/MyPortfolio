"""
Core app views - Home page and utilities
"""

from django.shortcuts import render
from apps.about.models import Profile
from apps.projects.models import Project
from apps.skills.models import SkillCategory
from apps.experience.models import Experience


def home(request):
    """
    Home page view
    """
    context = {
        'profile': Profile.objects.filter(is_active=True).first(),
        'featured_projects': Project.objects.filter(is_featured=True)[:3],
        'skill_categories': SkillCategory.objects.all()[:3],
        'latest_experience': Experience.objects.first(),
    }
    return render(request, 'home.html', context)
