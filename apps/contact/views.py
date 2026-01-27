"""
Contact app views
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from .models import ContactSubmission
from .forms import ContactForm


def contact(request):
    """
    Contact page with form and real-time email notifications
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Create submission
            submission = form.save(commit=False)
            # Get IP address
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                submission.ip_address = x_forwarded_for.split(',')[0]
            else:
                submission.ip_address = request.META.get('REMOTE_ADDR')
            # Get user agent
            submission.user_agent = request.META.get('HTTP_USER_AGENT', '')
            submission.save()
            
            # Send real-time email notification to admin
            try:
                admin_subject = f'New Contact Form Submission from {submission.name}'
                admin_message = f"""
New contact form submission received:

Name: {submission.name}
Email: {submission.email}
Subject: {submission.subject}

Message:
{submission.message}

Submitted at: {submission.created_at}
IP Address: {submission.ip_address}
                """
                send_mail(
                    admin_subject,
                    admin_message,
                    settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@portfolio.com',
                    ['rahullohra987@gmail.com'],  # Admin email
                    fail_silently=True,
                )
                
                # Send confirmation email to user
                user_subject = 'Thank you for contacting Rahul Lohra'
                user_message = f"""
Hi {submission.name},

Thank you for reaching out! I have received your message and will get back to you as soon as possible.

Your message:
Subject: {submission.subject}
{submission.message}

Best regards,
Rahul Lohra
Full Stack Developer | Backend Engineer | ML Specialist

Email: rahullohra987@gmail.com
GitHub: github.com/rahullo
LinkedIn: linkedin.com/in/rahul-lohra
                """
                send_mail(
                    user_subject,
                    user_message,
                    settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@portfolio.com',
                    [submission.email],
                    fail_silently=True,
                )
            except Exception as e:
                # Log the error but don't fail the submission
                print(f"Email sending failed: {e}")
            
            messages.success(request, '✅ Thank you for your message! I will get back to you soon. A confirmation email has been sent to your inbox.')
            return redirect('contact:contact')
        else:
            messages.error(request, '❌ Please correct the errors below.')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'contact/contact.html', context)
