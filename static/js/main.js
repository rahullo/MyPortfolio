// Portfolio Website - Main JavaScript

document.addEventListener('DOMContentLoaded', function () {
    // ===== Dark Mode Toggle =====
    const themeToggle = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement;

    // Check for saved theme preference or default to dark mode
    const currentTheme = localStorage.getItem('theme') || 'dark';
    htmlElement.setAttribute('data-theme', currentTheme);
    updateThemeIcon(currentTheme);

    if (themeToggle) {
        themeToggle.addEventListener('click', function () {
            const currentTheme = htmlElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

            htmlElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeIcon(newTheme);

            // Add animation effect
            this.style.transform = 'rotate(360deg)';
            setTimeout(() => {
                this.style.transform = '';
            }, 300);
        });
    }

    function updateThemeIcon(theme) {
        if (themeToggle) {
            const icon = themeToggle.querySelector('i');
            if (theme === 'dark') {
                icon.className = 'fas fa-sun';
            } else {
                icon.className = 'fas fa-moon';
            }
        }
    }

    // ===== Smooth scrolling for anchor links =====
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // ===== Add active class to current nav item =====
    const currentLocation = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentLocation) {
            link.classList.add('active');
        }
    });

    // ===== Form validation enhancement =====
    const forms = document.querySelectorAll('.needs-validation');
    forms.forEach(form => {
        form.addEventListener('submit', function (event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });

    // ===== Fade in animations on scroll =====
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.card, .timeline-item, .security-feature').forEach(el => {
        observer.observe(el);
    });

    // ===== Auto-dismiss alerts after 5 seconds =====
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            if (typeof bootstrap !== 'undefined' && bootstrap.Alert) {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }
        }, 5000);
    });

    // ===== Real-time Contact Form Enhancement =====
    const contactForm = document.querySelector('#contact-form');
    if (contactForm) {
        const submitBtn = contactForm.querySelector('button[type="submit"]');
        const originalBtnText = submitBtn ? submitBtn.innerHTML : '';

        contactForm.addEventListener('submit', function (e) {
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
            }

            // Form will submit normally, but we show loading state
            setTimeout(() => {
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalBtnText;
                }
            }, 3000);
        });

        // Real-time validation feedback
        const inputs = contactForm.querySelectorAll('input, textarea');
        inputs.forEach(input => {
            input.addEventListener('blur', function () {
                if (this.value.trim() !== '') {
                    this.classList.add('is-valid');
                    this.classList.remove('is-invalid');
                } else if (this.hasAttribute('required')) {
                    this.classList.add('is-invalid');
                    this.classList.remove('is-valid');
                }
            });

            input.addEventListener('input', function () {
                if (this.classList.contains('is-invalid') && this.value.trim() !== '') {
                    this.classList.remove('is-invalid');
                    this.classList.add('is-valid');
                }
            });
        });
    }

    // ===== Navbar scroll effect =====
    let lastScroll = 0;
    const navbar = document.querySelector('.navbar');

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;

        if (currentScroll > 100) {
            navbar.style.boxShadow = 'var(--shadow-lg)';
        } else {
            navbar.style.boxShadow = 'var(--shadow-sm)';
        }

        lastScroll = currentScroll;
    });

    // ===== Add pulse animation to CTA buttons =====
    const ctaButtons = document.querySelectorAll('.hero-section .btn-primary');
    ctaButtons.forEach(btn => {
        btn.classList.add('pulse');
    });
});

// ===== Email notification helper (for future enhancement) =====
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.body.appendChild(notification);

    setTimeout(() => {
        notification.remove();
    }, 5000);
}
