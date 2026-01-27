
import os
import django
import sys

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
django.setup()

from apps.about.models import Profile
from apps.skills.models import SkillCategory, Skill
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

if __name__ == '__main__':
    seed_data()
