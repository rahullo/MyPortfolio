# Rahul Lohra - Professional Portfolio Website

Enterprise-grade portfolio website built with Django and MySQL, showcasing Full Stack Development, Backend Engineering, and Machine Learning expertise with government-level security practices.

## 🎯 Features

- **Enterprise Security**: PBKDF2-SHA256 password hashing, Django Axes brute-force protection, CSRF protection
- **Modular Architecture**: Clean separation of concerns with dedicated Django apps
- **MySQL Database**: Production-ready relational database
- **Responsive Design**: Mobile-first Bootstrap 5 UI
- **SEO Optimized**: Meta tags, semantic HTML, Open Graph support
- **Admin Dashboard**: Full CRUD operations for content management
- **Contact Form**: Secure form with IP tracking and validation

## 🛠️ Tech Stack

### Backend
- Python 3.11+
- Django 5.0.1
- Django REST Framework
- MySQL
- Gunicorn (production server)

### Frontend
- HTML5 / CSS3
- Bootstrap 5
- JavaScript (Vanilla)
- Font Awesome icons
- Google Fonts (Inter)

### Security
- PBKDF2-SHA256 password hashing
- Django Axes (brute-force protection)
- CSRF protection
- Secure headers (X-Frame-Options, etc.)
- Environment-based configuration

## 📋 Prerequisites

- Python 3.11 or higher
- MySQL 8.0 or higher
- pip (Python package manager)

## 🚀 Installation

### 1. Clone the repository
```bash
git clone <repository-url>
cd portfolio
```

### 2. Create virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up MySQL database
```sql
CREATE DATABASE portfolio_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'portfolio_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON portfolio_db.* TO 'portfolio_user'@'localhost';
FLUSH PRIVILEGES;
```

### 5. Configure environment variables
Copy `.env.example` to `.env` and update with your settings:
```bash
cp .env.example .env
```

Edit `.env`:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=portfolio_db
DB_USER=portfolio_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
```

### 6. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create superuser
```bash
python manage.py createsuperuser
```

### 8. Seed database with portfolio data
```bash
python manage.py seed_data
```

### 9. Run development server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` to view the website.

## 📁 Project Structure

```
portfolio/
├── config/                 # Project configuration
│   ├── settings/
│   │   ├── base.py        # Base settings
│   │   ├── development.py # Development settings
│   │   └── production.py  # Production settings
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/                   # Django applications
│   ├── core/              # Base app (home page)
│   ├── about/             # About section
│   ├── skills/            # Technical skills
│   ├── experience/        # Work experience
│   ├── projects/          # Portfolio projects
│   ├── education/         # Academic background
│   ├── security/          # Security features
│   ├── contact/           # Contact form
│   ├── accounts/          # User authentication
│   └── dashboard/         # Admin CMS
├── static/                 # Static files
│   ├── css/
│   ├── js/
│   ├── images/
│   └── fonts/
├── templates/              # HTML templates
├── media/                  # User uploads
├── logs/                   # Application logs
├── requirements.txt
├── .env.example
└── README.md
```

## 🎨 Customization

### Adding New Content

1. **Login to Admin**: Visit `/admin` and login with superuser credentials
2. **Manage Content**: Use the admin interface to add/edit:
   - Profile information
   - Skills and categories
   - Work experience
   - Projects
   - Education
   - Security features
   - View contact submissions

### Modifying Styles

Edit `static/css/main.css` to customize:
- Color scheme (CSS variables)
- Typography
- Component styles
- Responsive breakpoints

## 🔒 Security Features

- **Password Hashing**: PBKDF2-SHA256 with multiple iterations
- **Brute-Force Protection**: Django Axes with configurable lockout
- **CSRF Protection**: Enabled on all forms
- **Secure Headers**: X-Frame-Options, X-Content-Type-Options, etc.
- **Input Validation**: Form validation and sanitization
- **SQL Injection Protection**: Django ORM parameterized queries

## 🚢 Deployment

### Production Checklist

1. **Update settings**:
   ```env
   DEBUG=False
   SECRET_KEY=<strong-random-key>
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   ```

2. **Collect static files**:
   ```bash
   python manage.py collectstatic
   ```

3. **Run security check**:
   ```bash
   python manage.py check --deploy
   ```

4. **Configure Gunicorn**:
   ```bash
   gunicorn config.wsgi:application --bind 0.0.0.0:8000
   ```

5. **Set up Nginx** (see `nginx.conf.example`)

6. **Enable HTTPS** with Let's Encrypt

## 📊 Database Schema

### Key Models

- **Profile**: Professional information and bio
- **SkillCategory**: Skill groupings (Languages, Frameworks, etc.)
- **Skill**: Individual skills with proficiency levels
- **Experience**: Work history with highlights and technologies
- **Project**: Portfolio projects with features and images
- **Education**: Academic qualifications
- **SecurityFeature**: Security implementations showcase
- **ContactSubmission**: Contact form submissions

## 🧪 Testing

Run tests:
```bash
python manage.py test
```

Run with coverage:
```bash
coverage run --source='.' manage.py test
coverage report
```

## 📝 Management Commands

- `python manage.py seed_data` - Populate database with portfolio data
- `python manage.py createsuperuser` - Create admin user
- `python manage.py collectstatic` - Collect static files for production

## 🤝 Contributing

This is a personal portfolio project. However, if you find bugs or have suggestions:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Rahul Lohra**
- Email: rahullohra987@gmail.com
- GitHub: [@rahullo](https://github.com/rahullo)
- LinkedIn: [rahul-lohra](https://linkedin.com/in/rahul-lohra)

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap Team
- Font Awesome
- CERT-In for internship opportunity

---

**Built with ❤️ using Django + MySQL**
