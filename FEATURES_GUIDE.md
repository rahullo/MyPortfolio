# Portfolio Website - New Features Setup Guide

## 🎨 What's New

### 1. **Dark/Light Mode Toggle**
- Floating toggle button in bottom-right corner
- Smooth theme transitions
- Persistent theme preference (saved in localStorage)
- Vibrant color schemes for both modes

### 2. **Enhanced Color Scheme**
- **Primary**: Vibrant indigo (#6366f1)
- **Secondary**: Hot pink (#ec4899)
- **Accent**: Amber (#f59e0b)
- **Gradients**: Multiple vibrant gradients throughout
- **Dark Mode**: Carefully crafted dark theme with proper contrast

### 3. **Real-time Contact System**
- Instant email notifications when someone contacts you
- Automatic confirmation email sent to the user
- Real-time form validation with visual feedback
- Loading states during form submission
- IP address and user agent tracking

## 🚀 Quick Start

### Step 1: Test Dark Mode
1. Run the development server: `python manage.py runserver`
2. Visit any page
3. Click the floating button in the bottom-right corner
4. Theme preference is automatically saved

### Step 2: Configure Email (Optional but Recommended)

For real-time email notifications, update your `.env` file:

```env
# Email Configuration for Real-time Notifications
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
DEFAULT_FROM_EMAIL=noreply@yourportfolio.com
```

**For Gmail:**
1. Go to Google Account Settings
2. Enable 2-Factor Authentication
3. Generate an "App Password" for Django
4. Use that app password in `EMAIL_HOST_PASSWORD`

### Step 3: Test Contact Form
1. Navigate to `/contact`
2. Fill out the form
3. Submit
4. Check your email (both admin and user will receive emails)
5. If using console backend, check terminal for email output

## 🎯 Features Breakdown

### Dark Mode Implementation
- **CSS Variables**: All colors use CSS custom properties
- **Theme Attribute**: `data-theme="dark"` or `data-theme="light"`
- **JavaScript**: Automatic theme detection and persistence
- **Smooth Transitions**: All elements transition smoothly between themes

### Real-time Contact Features
- **Dual Email System**:
  - Admin receives notification with full details
  - User receives confirmation email
- **Form Validation**:
  - Real-time validation as user types
  - Visual feedback (green/red borders)
  - Loading spinner during submission
- **Error Handling**:
  - Graceful email failure (doesn't break form)
  - User-friendly error messages with emojis

### Enhanced UX
- **Scroll Animations**: Elements fade in as you scroll
- **Navbar Shadow**: Increases on scroll
- **Pulse Animation**: CTA buttons have subtle pulse
- **Smooth Scrolling**: Anchor links scroll smoothly
- **Auto-dismiss Alerts**: Messages disappear after 5 seconds

## 🎨 Color Palette

### Light Mode
- Primary: `#6366f1` (Indigo)
- Secondary: `#ec4899` (Pink)
- Accent: `#f59e0b` (Amber)
- Background: `#f9fafb` (Light Gray)
- Text: `#1f2937` (Dark Gray)

### Dark Mode
- Primary: `#818cf8` (Light Indigo)
- Secondary: `#f472b6` (Light Pink)
- Accent: `#fbbf24` (Light Amber)
- Background: `#1f2937` (Dark Gray)
- Text: `#f9fafb` (Light Gray)

### Gradients
- Primary: Purple to Violet
- Secondary: Pink to Red
- Accent: Blue to Cyan
- Success: Green to Teal

## 📧 Email Templates

### Admin Notification
```
Subject: New Contact Form Submission from [Name]

New contact form submission received:

Name: [Name]
Email: [Email]
Subject: [Subject]

Message:
[Message]

Submitted at: [Timestamp]
IP Address: [IP]
```

### User Confirmation
```
Subject: Thank you for contacting Rahul Lohra

Hi [Name],

Thank you for reaching out! I have received your message 
and will get back to you as soon as possible.

Your message:
Subject: [Subject]
[Message]

Best regards,
Rahul Lohra
```

## 🔧 Customization

### Change Theme Colors
Edit `static/css/main.css`:
```css
:root {
    --primary-color: #your-color;
    --secondary-color: #your-color;
    /* etc. */
}
```

### Modify Email Recipients
Edit `apps/contact/views.py`:
```python
send_mail(
    admin_subject,
    admin_message,
    settings.DEFAULT_FROM_EMAIL,
    ['your_email@example.com'],  # Change this
    fail_silently=True,
)
```

### Adjust Toggle Button Position
Edit `static/css/main.css`:
```css
.theme-toggle {
    bottom: 2rem;  /* Change this */
    right: 2rem;   /* Change this */
}
```

## 🧪 Testing Checklist

- [ ] Dark mode toggle works
- [ ] Theme persists after page reload
- [ ] Contact form submits successfully
- [ ] Emails are sent (check terminal if using console backend)
- [ ] Form validation shows real-time feedback
- [ ] Loading spinner appears during submission
- [ ] Success message displays after submission
- [ ] All pages look good in both light and dark mode
- [ ] Mobile responsive (test on phone)
- [ ] Gradients and colors are vibrant

## 🐛 Troubleshooting

### Dark Mode Not Working
- Check browser console for JavaScript errors
- Ensure `static/js/main.js` is loaded
- Clear browser cache

### Emails Not Sending
- Check `.env` file configuration
- Verify EMAIL_BACKEND setting
- For Gmail, ensure app password is correct
- Check terminal for error messages

### Colors Look Wrong
- Hard refresh browser (Ctrl+Shift+R)
- Check if `static/css/main.css` is loaded
- Inspect element to verify CSS variables

## 📱 Mobile Optimization

- Toggle button is smaller on mobile (50px vs 60px)
- Positioned at bottom-right with 1rem margin
- All colors and gradients work on mobile
- Form is fully responsive

## 🎉 Next Steps

1. **Test everything** in both light and dark modes
2. **Configure email** for production use
3. **Customize colors** to match your brand
4. **Add your logo** to replace the code icon
5. **Deploy** and share your vibrant portfolio!

---

**Built with ❤️ - Now with Dark Mode & Real-time Contact!**
