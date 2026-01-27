"""
Projects app views
"""

from django.shortcuts import render, get_object_or_404
from .models import Project


def project_list(request):
    """
    Projects listing page
    """
    projects_standard = Project.objects.filter(category='standard')
    projects_freelance = Project.objects.filter(category='freelance')
    context = {
        'projects_standard': projects_standard,
        'projects_freelance': projects_freelance,
    }
    return render(request, 'projects/project_list.html', context)


def project_detail(request, slug):
    """
    Individual project detail page
    """
    project = get_object_or_404(Project, slug=slug)
    context = {
        'project': project,
        'tech_stack_list': project.get_tech_stack_list(),
    }
    return render(request, 'projects/project_detail.html', context)
