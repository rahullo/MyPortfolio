import os
import django
from django.utils import timezone
from datetime import date

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

from apps.projects.models import Project

def create_freelance_projects():
    # Project 1: E-commerce Dashboard
    p1, created = Project.objects.get_or_create(
        title="E-Shop Analytics Dashboard",
        defaults={
            # "description" field does not exist, using detailed_description instead
            "short_description": "Real-time sales and inventory analytics for high-volume e-commerce.",
            "detailed_description": "Built a custom dashboard processing 50k+ daily transactions. Features include real-time sales tracking, inventory forecasting, and customer segmentation visualizations. Reduced reporting time by 90%.",
            "tech_stack": "React, Django, PostgreSQL, Redis, Chart.js",
            "start_date": date(2025, 1, 15),
            "category": "freelance",
            "is_featured": False,
            "live_url": "https://dashboard-demo.example.com",
            "order": 1
        }
    )
    if not created:
        p1.category = 'freelance'
        p1.save()
        print(f"Updated {p1.title}")
    else:
        print(f"Created {p1.title}")

    # Project 2: Corporate Booking System
    p2, created = Project.objects.get_or_create(
        title="CorpMeet Booking System",
        defaults={
            "short_description": "Internal meeting room and resource booking system for a mid-sized corp.",
            "detailed_description": "Developed a streamlined booking interface integrated with Outlook and Google Calendar. Features include conflict resolution, recurring bookings, and resource management.",
            "tech_stack": "Vue.js, Python, FastAPI, Docker",
            "start_date": date(2024, 11, 10),
            "category": "freelance",
            "is_featured": False,
            "live_url": "https://booking.example.com",
            "order": 2
        }
    )
    if not created:
        p2.category = 'freelance'
        p2.save()
        print(f"Updated {p2.title}")
    else:
        print(f"Created {p2.title}")

if __name__ == "__main__":
    create_freelance_projects()
