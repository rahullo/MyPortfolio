"""
Education app views
"""

from django.shortcuts import render
from .models import Education


def education(request):
    """
    Education page view
    """
    context = {
        'education_list': Education.objects.all(),
    }
    return render(request, 'education/education.html', context)
