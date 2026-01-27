"""
Django management command to seed the database with Rahul Lohra's portfolio data
Usage: python manage.py seed_data
"""

from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date

from apps.about.models import Profile
from apps.skills.models import SkillCategory, Skill
from apps.experience.models import Experience, ExperienceHighlight, ExperienceTechnology
from apps.projects.models import Project, ProjectFeature
from apps.education.models import Education
from apps.security.models import SecurityFeature


class Command(BaseCommand):
    help = 'Seeds the database with Rahul Lohra portfolio data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting data seeding...'))

        # Clear existing data (optional - comment out if you want to keep existing data)
        self.stdout.write('Clearing existing data...')
        Profile.objects.all().delete()
        SkillCategory.objects.all().delete()
        Experience.objects.all().delete()
        Project.objects.all().delete()
        Education.objects.all().delete()
        SecurityFeature.objects.all().delete()

        # Create Profile
        self.stdout.write('Creating profile...')
        profile = Profile.objects.create(
            name="Rahul Lohra",
            role="Full Stack Developer | Backend-Heavy | Machine Learning",
            email="rahullohra987@gmail.com",
            github_url="https://github.com/rahullo",
            linkedin_url="https://linkedin.com/in/rahul-lohra",
            summary="""Backend-focused Full Stack Developer with government-level internship experience at CERT-In. 
            Specialized in building secure, scalable Django applications with enterprise-grade security practices. 
            Strong foundation in Machine Learning and data privacy, with proven ability to deliver production-ready systems 
            that improve operational efficiency. Passionate about clean code, system architecture, and security-first development.""",
            is_active=True,
            meta_title="Rahul Lohra - Full Stack Developer | Backend Engineer | ML Specialist",
            meta_description="Portfolio of Rahul Lohra - Full Stack Developer specializing in Django, Python, and Machine Learning with CERT-In internship experience"
        )

        # Create Skill Categories and Skills
        self.stdout.write('Creating skills...')
        
        # Programming Languages
        prog_lang = SkillCategory.objects.create(name="Programming Languages", icon="fa-code", order=1)
        Skill.objects.create(category=prog_lang, name="Python", proficiency=95, icon="fa-python", order=1)
        Skill.objects.create(category=prog_lang, name="JavaScript", proficiency=85, icon="fa-js", order=2)
        Skill.objects.create(category=prog_lang, name="SQL", proficiency=80, icon="fa-database", order=3)
        Skill.objects.create(category=prog_lang, name="HTML / CSS", proficiency=85, icon="fa-html5", order=4)

        # Frameworks & Libraries
        frameworks = SkillCategory.objects.create(name="Frameworks & Libraries", icon="fa-layer-group", order=2)
        Skill.objects.create(category=frameworks, name="Django", proficiency=90, icon="fa-server", order=1)
        Skill.objects.create(category=frameworks, name="Django REST Framework", proficiency=85, icon="fa-cogs", order=2)
        Skill.objects.create(category=frameworks, name="Flask", proficiency=80, icon="fa-flask", order=3)
        Skill.objects.create(category=frameworks, name="React.js", proficiency=75, icon="fa-react", order=4)
        Skill.objects.create(category=frameworks, name="Node.js", proficiency=70, icon="fa-node-js", order=5)
        Skill.objects.create(category=frameworks, name="Express.js", proficiency=70, icon="fa-server", order=6)
        Skill.objects.create(category=frameworks, name="NumPy", proficiency=80, icon="fa-chart-line", order=7)
        Skill.objects.create(category=frameworks, name="Pandas", proficiency=80, icon="fa-table", order=8)
        Skill.objects.create(category=frameworks, name="Scikit-learn", proficiency=75, icon="fa-brain", order=9)
        Skill.objects.create(category=frameworks, name="Matplotlib", proficiency=70, icon="fa-chart-bar", order=10)

        # Databases
        databases = SkillCategory.objects.create(name="Databases", icon="fa-database", order=3)
        Skill.objects.create(category=databases, name="MySQL", proficiency=85, icon="fa-database", order=1)
        Skill.objects.create(category=databases, name="PostgreSQL", proficiency=80, icon="fa-database", order=2)
        Skill.objects.create(category=databases, name="MongoDB", proficiency=75, icon="fa-leaf", order=3)

        # Tools & Technologies
        tools = SkillCategory.objects.create(name="Tools & Technologies", icon="fa-tools", order=4)
        Skill.objects.create(category=tools, name="Git / GitHub", proficiency=90, icon="fa-git-alt", order=1)
        Skill.objects.create(category=tools, name="REST APIs", proficiency=90, icon="fa-exchange-alt", order=2)
        Skill.objects.create(category=tools, name="Docker", proficiency=70, icon="fa-docker", order=3)
        Skill.objects.create(category=tools, name="Jupyter Notebook", proficiency=80, icon="fa-book", order=4)
        Skill.objects.create(category=tools, name="Figma", proficiency=65, icon="fa-figma", order=5)
        Skill.objects.create(category=tools, name="Agile / Scrum", proficiency=85, icon="fa-tasks", order=6)

        # Core Competencies
        competencies = SkillCategory.objects.create(name="Core Competencies", icon="fa-star", order=5)
        Skill.objects.create(category=competencies, name="Full-Stack Development", proficiency=90, order=1)
        Skill.objects.create(category=competencies, name="Backend Architecture", proficiency=90, order=2)
        Skill.objects.create(category=competencies, name="Machine Learning", proficiency=80, order=3)
        Skill.objects.create(category=competencies, name="API Design", proficiency=85, order=4)
        Skill.objects.create(category=competencies, name="Data Analysis", proficiency=80, order=5)
        Skill.objects.create(category=competencies, name="System Design", proficiency=85, order=6)
        Skill.objects.create(category=competencies, name="Security Implementation", proficiency=85, order=7)
        Skill.objects.create(category=competencies, name="Technical Documentation", proficiency=85, order=8)
        Skill.objects.create(category=competencies, name="Team Collaboration", proficiency=90, order=9)

        # Create Experience
        self.stdout.write('Creating experience...')
        cert_in = Experience.objects.create(
            title="Software Engineering Intern",
            company="CERT-In (Indian Computer Emergency Response Team)",
            location="Delhi, India",
            start_date=date(2025, 2, 1),
            end_date=date(2025, 8, 31),
            is_current=False,
            description="""Worked as a Software Engineering Intern at India's national cybersecurity agency, 
            developing enterprise-grade web applications and implementing security-first development practices.""",
            order=0
        )

        # Add highlights
        ExperienceHighlight.objects.create(
            experience=cert_in,
            text="Architected and deployed a full-stack Django web application serving 100+ internal users, improving workflow efficiency by 40% via automated document processing and role-based access control",
            order=1
        )
        ExperienceHighlight.objects.create(
            experience=cert_in,
            text="Implemented enterprise-grade security architecture using PBKDF2-SHA256 password hashing, multi-factor authentication with OTP validation, and Django Axes for brute-force attack protection, achieving zero security incidents",
            order=2
        )
        ExperienceHighlight.objects.create(
            experience=cert_in,
            text="Designed and integrated RESTful APIs with Twilio and Gmail services for real-time authentication workflows and automated email notifications, reducing manual verification time by 60%",
            order=3
        )
        ExperienceHighlight.objects.create(
            experience=cert_in,
            text="Collaborated with 8+ cross-functional team members using Agile/Scrum, participating in standups, sprint planning, and code reviews",
            order=4
        )

        # Add technologies
        for tech in ["Django", "Python", "MySQL", "REST APIs", "Twilio API", "Gmail API", "PBKDF2-SHA256", "Django Axes", "OTP Authentication", "Agile/Scrum"]:
            ExperienceTechnology.objects.create(experience=cert_in, technology=tech)

        # Create Projects
        self.stdout.write('Creating projects...')
        
        # Project 1: AI-Powered File Converter
        project1 = Project.objects.create(
            title="AI-Powered File Converter & Summarizer",
            short_description="Intelligent document processing platform with React.js frontend and Django/Flask backend enabling file format conversion and AI-powered PDF summarization",
            detailed_description="""Built a comprehensive document processing platform that combines file format conversion 
            with intelligent AI-powered summarization capabilities. The system features a modern React.js frontend with 
            real-time progress tracking and a robust Django/Flask backend with asynchronous API processing.
            
            The platform enables users to convert between multiple file formats seamlessly while providing AI-powered 
            summarization for PDF documents. Integrated NLP models achieve 90%+ accuracy in content extraction and 
            deliver processing speeds 5× faster than manual review.
            
            Implemented robust error handling, request validation, and achieved 99% uptime through careful system design 
            and monitoring. The frontend uses modern React patterns including hooks and Context API for state management.""",
            tech_stack="React.js, Django, Flask, NLP, REST APIs, Python, JavaScript, Machine Learning",
            start_date=date(2024, 11, 1),
            end_date=date(2025, 2, 28),
            github_url="https://github.com/rahullo",
            is_featured=True,
            order=1,
            meta_title="AI File Converter - Intelligent Document Processing",
            meta_description="AI-powered file conversion and PDF summarization platform built with React, Django, and NLP"
        )

        # Add features for Project 1
        ProjectFeature.objects.create(
            project=project1,
            feature="Multi-format file conversion with support for PDF, DOCX, TXT, and more",
            order=1
        )
        ProjectFeature.objects.create(
            project=project1,
            feature="AI-powered PDF summarization using NLP models with 90%+ accuracy",
            order=2
        )
        ProjectFeature.objects.create(
            project=project1,
            feature="Asynchronous backend APIs with robust error handling and request validation",
            order=3
        )
        ProjectFeature.objects.create(
            project=project1,
            feature="Real-time progress tracking for long-running tasks",
            order=4
        )
        ProjectFeature.objects.create(
            project=project1,
            feature="Modern React frontend with hooks and Context API",
            order=5
        )
        ProjectFeature.objects.create(
            project=project1,
            feature="99% uptime with comprehensive monitoring and error handling",
            order=6
        )

        # Project 2: Federated Learning System
        project2 = Project.objects.create(
            title="Federated Learning System",
            short_description="Privacy-preserving machine learning framework simulating distributed training on medical insurance data without raw data sharing",
            detailed_description="""Developed a privacy-preserving Federated Learning framework that enables collaborative 
            machine learning without sharing raw data. The system simulates 5 distributed clients performing decentralized 
            training on medical insurance data, ensuring data privacy while maintaining model accuracy.
            
            Implemented a complete ML pipeline using SGDRegressor with advanced preprocessing including normalization and 
            feature engineering. Developed custom weight aggregation algorithms to combine model updates from distributed 
            clients, achieving 85% prediction accuracy while maintaining complete data privacy.
            
            The system is built as a modular, well-documented Python pipeline with comprehensive unit tests for 
            reproducibility. This project demonstrates deep understanding of privacy-preserving ML techniques and 
            distributed system design.""",
            tech_stack="Python, Scikit-learn, Machine Learning, Data Privacy, NumPy, Pandas",
            start_date=date(2024, 3, 1),
            end_date=date(2024, 8, 31),
            github_url="https://github.com/rahullo",
            is_featured=True,
            order=2,
            meta_title="Federated Learning System - Privacy-Preserving ML",
            meta_description="Distributed machine learning system with privacy preservation on medical insurance data"
        )

        # Add features for Project 2
        ProjectFeature.objects.create(
            project=project2,
            feature="Privacy-preserving federated learning with no raw data sharing",
            order=1
        )
        ProjectFeature.objects.create(
            project=project2,
            feature="5 distributed clients with decentralized training architecture",
            order=2
        )
        ProjectFeature.objects.create(
            project=project2,
            feature="ML pipeline with SGDRegressor, normalization, and feature engineering",
            order=3
        )
        ProjectFeature.objects.create(
            project=project2,
            feature="Custom weight aggregation algorithm for model updates",
            order=4
        )
        ProjectFeature.objects.create(
            project=project2,
            feature="85% prediction accuracy on medical insurance data",
            order=5
        )
        ProjectFeature.objects.create(
            project=project2,
            feature="Modular Python pipeline with comprehensive unit tests",
            order=6
        )

        # Create Education
        self.stdout.write('Creating education...')
        
        Education.objects.create(
            degree="Master of Computer Applications (MCA)",
            field="Computer Applications",
            institution="Banaras Hindu University (BHU)",
            location="Varanasi, India",
            cgpa=7.3,
            max_cgpa=10.0,
            start_date=date(2023, 9, 1),
            end_date=date(2025, 6, 30),
            order=1
        )

        Education.objects.create(
            degree="Bachelor of Technology in Information Technology",
            field="Information Technology",
            institution="Dr. Shyama Prasad Mukherjee University",
            location="Ranchi, India",
            cgpa=8.61,
            max_cgpa=10.0,
            start_date=date(2020, 6, 1),
            end_date=date(2023, 8, 31),
            order=2
        )

        # Create Security Features
        self.stdout.write('Creating security features...')
        
        SecurityFeature.objects.create(
            title="PBKDF2-SHA256 Password Hashing",
            category="authentication",
            description="""Implemented industry-standard PBKDF2-SHA256 password hashing algorithm for secure password storage. 
            This cryptographic hash function applies multiple iterations of SHA-256, making brute-force attacks computationally 
            infeasible. Used extensively in the CERT-In internship project to protect user credentials.""",
            icon="fa-key",
            order=1
        )

        SecurityFeature.objects.create(
            title="Multi-Factor Authentication (OTP)",
            category="authentication",
            description="""Designed and implemented OTP-based multi-factor authentication system integrated with Twilio API. 
            Provides an additional security layer beyond passwords, significantly reducing unauthorized access risks. 
            Implemented real-time OTP generation, validation, and expiration mechanisms.""",
            icon="fa-mobile-alt",
            order=2
        )

        SecurityFeature.objects.create(
            title="Django Axes - Brute Force Protection",
            category="authentication",
            description="""Integrated Django Axes middleware to protect against brute-force login attacks. Implements 
            intelligent lockout mechanisms based on failed login attempts, IP addresses, and user combinations. 
            Achieved zero security incidents during CERT-In internship through this implementation.""",
            icon="fa-shield-alt",
            order=3
        )

        SecurityFeature.objects.create(
            title="RESTful API Security",
            category="api_security",
            description="""Implemented comprehensive API security measures including authentication tokens, rate limiting, 
            input validation, and CORS policies. Designed secure API endpoints for Twilio and Gmail integrations with 
            proper error handling and logging.""",
            icon="fa-exchange-alt",
            order=4
        )

        SecurityFeature.objects.create(
            title="Role-Based Access Control (RBAC)",
            category="authentication",
            description="""Architected and implemented granular role-based access control system for the CERT-In application. 
            Defined user roles, permissions, and access levels to ensure users only access authorized resources. 
            Improved security posture while maintaining operational efficiency.""",
            icon="fa-users-cog",
            order=5
        )

        SecurityFeature.objects.create(
            title="OWASP Security Awareness",
            category="compliance",
            description="""Strong understanding of OWASP Top 10 security vulnerabilities and mitigation strategies. 
            Applied security best practices including protection against SQL injection, XSS, CSRF, and other common 
            web application vulnerabilities. Developed with security-first mindset gained from CERT-In experience.""",
            icon="fa-bug",
            order=6
        )

        SecurityFeature.objects.create(
            title="Secure Data Transmission",
            category="data_protection",
            description="""Implemented HTTPS/TLS for all data transmission, ensuring end-to-end encryption. 
            Configured secure headers including HSTS, X-Frame-Options, and Content-Security-Policy to prevent 
            common attack vectors.""",
            icon="fa-lock",
            order=7
        )

        self.stdout.write(self.style.SUCCESS('✓ Data seeding completed successfully!'))
        self.stdout.write(self.style.SUCCESS(f'✓ Created profile for {profile.name}'))
        self.stdout.write(self.style.SUCCESS(f'✓ Created {SkillCategory.objects.count()} skill categories'))
        self.stdout.write(self.style.SUCCESS(f'✓ Created {Skill.objects.count()} skills'))
        self.stdout.write(self.style.SUCCESS(f'✓ Created {Experience.objects.count()} experience entries'))
        self.stdout.write(self.style.SUCCESS(f'✓ Created {Project.objects.count()} projects'))
        self.stdout.write(self.style.SUCCESS(f'✓ Created {Education.objects.count()} education entries'))
        self.stdout.write(self.style.SUCCESS(f'✓ Created {SecurityFeature.objects.count()} security features'))
