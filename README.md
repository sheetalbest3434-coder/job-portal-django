# JobHub - Job Portal

A modern Django-based job portal web application to browse and post job listings.

## Features ✨

- 🏠 Beautiful home page with modern design
- 💼 Browse job listings
- ➕ Post new job opportunities
- 🎨 Responsive and attractive UI
- 🚀 Built with Django and vanilla CSS

## Tech Stack

- **Backend**: Django 6.0
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, Font Awesome Icons
- **Python**: 3.x

## Installation

### Prerequisites
- Python 3.x installed
- pip package manager

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/jobhub.git
cd jobhub
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install django
```

4. **Navigate to project**
```bash
cd jobportal
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Create superuser (Admin)**
```bash
python manage.py createsuperuser
```

7. **Start the development server**
```bash
python manage.py runserver
```

8. **Access the application**
- Home Page: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/

## Project Structure

```
jobportal/
├── jobportal/           # Main project settings
│   ├── settings.py      # Django configuration
│   ├── urls.py          # URL routing
│   ├── wsgi.py          # WSGI configuration
│   └── asgi.py          # ASGI configuration
├── jobs/                # Jobs app
│   ├── models.py        # Database models
│   ├── views.py         # View functions
│   ├── urls.py          # App URLs
│   ├── templates/       # HTML templates
│   │   ├── home.html
│   │   └── jobs/
│   │       └── job_list.html
│   └── static/          # CSS & static files
│       └── css/
│           └── jobs.css
├── manage.py            # Django management tool
└── db.sqlite3           # Database file
```

## Usage

### Home Page
- Visit the home page to see the portal overview
- Click "Explore Jobs Now" to view all job listings

### Browse Jobs
- See all posted job opportunities
- Each job displays: Title, Company, Location, Salary

### Post a Job
- Fill in the job posting form with:
  - Job Title
  - Company Name
  - Location
  - Salary
- Click "Post Job" to add the job to the listings

## Features Coming Soon 🔜

- User authentication and profiles
- Job search and filtering
- Application system
- Job favorites/bookmarks
- Email notifications

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License

This project is open source and available under the MIT License.

## Contact

For questions or suggestions, please open an issue on GitHub.

---

**Happy Job Hunting! 🚀**
