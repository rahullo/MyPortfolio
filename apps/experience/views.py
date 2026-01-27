"""
Experience app views
"""

from django.shortcuts import render
from .models import Experience


def experience(request):
    """
    Experience page view
    """
    context = {
        'experiences': Experience.objects.prefetch_related('highlights', 'technologies').all(),
    }
    return render(request, 'experience/experience.html', context)
