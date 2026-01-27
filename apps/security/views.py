"""
Security app views
"""

from django.shortcuts import render
from .models import SecurityFeature


def security(request):
    """
    Security features showcase page
    """
    context = {
        'security_features': SecurityFeature.objects.all(),
        'features_by_category': {},
    }
    
    # Group features by category
    for feature in context['security_features']:
        category = feature.get_category_display()
        if category not in context['features_by_category']:
            context['features_by_category'][category] = []
        context['features_by_category'][category].append(feature)
    
    return render(request, 'security/security.html', context)
