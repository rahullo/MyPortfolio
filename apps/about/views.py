"""
About app views
"""

from django.shortcuts import render
from .models import Profile


def about(request):
    """
    About page view
    """
    context = {
        'profile': Profile.objects.filter(is_active=True).first(),
    }
    return render(request, 'about/about.html', context)
