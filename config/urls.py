"""
Main URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Apps
    path('', include('apps.core.urls')),
    path('about/', include('apps.about.urls')),
    path('skills/', include('apps.skills.urls')),
    path('experience/', include('apps.experience.urls')),
    path('projects/', include('apps.projects.urls')),
    path('education/', include('apps.education.urls')),
    path('security/', include('apps.security.urls')),
    path('contact/', include('apps.contact.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    # Debug toolbar
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns

# Customize admin site
admin.site.site_header = "Rahul Lohra Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Portfolio Administration"
