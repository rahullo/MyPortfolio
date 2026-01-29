
import os
import django
import sys

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
django.setup()

from apps.about.models import Profile
from apps.skills.models import SkillCategory, Skill
from apps.security.models import SecurityFeature
from django.contrib.auth import get_user_model

User = get_user_model()

def seed_data():
    # Create Superuser if not exists
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
        print("Created superuser 'admin' with password 'admin'")

    # Create Profile
    if not Profile.objects.exists():
        Profile.objects.create(
            name="Rahul Lohra",
            role="Full Stack Developer",
            summary="Passionate developer specializing in Python and React. Experienced Full Stack Developer with a background in secure application development.",
            email="rahullohra987@gmail.com",
            github_url="https://github.com/rahullo",
            linkedin_url="https://linkedin.com/in/rahul-lohra",
            is_active=True
        )
        print("Created default Profile")
    
    # Create Initial Skills
    if not SkillCategory.objects.exists():
        backend = SkillCategory.objects.create(name="Backend", icon="fas fa-server", order=1)
        frontend = SkillCategory.objects.create(name="Frontend", icon="fas fa-code", order=2)
        
        Skill.objects.create(category=backend, name="Python", proficiency=90)
        Skill.objects.create(category=backend, name="Django", proficiency=85)
        Skill.objects.create(category=frontend, name="React", proficiency=80)
        print("Created initial Skills")

    # Create Security Features
    if not SecurityFeature.objects.exists():
        security_features = [
            {
                "title": "Multi-Factor Authentication (MFA)",
                "category": "authentication",
                "description": "Implemented robust TOTP-based 2FA using time-based algorithms to ensure secure user access and prevent unauthorized logins using Django Two-Factor Authentication.",
                "icon": "fas fa-user-shield",
                "order": 1
            },
            {
                "title": "Military-Grade Encryption",
                "category": "data_protection",
                "description": "All sensitive user data is encrypted at rest using AES-256 standards. Passwords are hashed with PBKDF2-SHA256 with high iteration counts.",
                "icon": "fas fa-lock",
                "order": 2
            },
            {
                "title": "Rate Limiting & Throttling",
                "category": "api_security",
                "description": "Advanced request throttling configured at the gateway level to prevent DDoS attacks and abusive usage patterns.",
                "icon": "fas fa-shield-virus",
                "order": 3
            },
            {
                "title": "Automated Intrusion Detection",
                "category": "infrastructure",
                "description": "Real-time monitoring system that analyzes traffic patterns to detect and block suspicious IPs (Django Axes) automatically.",
                "icon": "fas fa-server",
                "order": 4
            },
            {
                "title": "OWASP Top 10 Mitigation",
                "category": "compliance",
                "description": "System architecture is hardened against common vulnerabilities including SQL Injection, XSS, and CSRF, strictly adhering to OWASP security guidelines.",
                "icon": "fas fa-clipboard-check",
                "order": 5
            }
        ]
        
        for feature in security_features:
            SecurityFeature.objects.create(**feature)
        print("Created Security Features")

if __name__ == '__main__':
    seed_data()
