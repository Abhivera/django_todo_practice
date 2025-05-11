# Django Todo App

A full-featured Todo application built with Django and PostgreSQL (Neon), featuring a clean interface and complete task management functionality.

![Django Todo App](https://via.placeholder.com/800x400?text=Django+Todo+App)

## Features

- Create, read, update, and delete tasks
- Mark tasks as complete/incomplete
- Responsive design with Bootstrap
- Admin interface for easy management
- PostgreSQL database with Neon cloud hosting

## Tech Stack

- Django 4.2+
- PostgreSQL (Neon)
- Bootstrap 5
- Python 3.8+

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-todo-app.git
   cd django-todo-app
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables by creating a `.env` file:
   ```
   # Database Configuration (Neon PostgreSQL)
   DB_NAME=todo_db
   DB_USER=postgres
   DB_PASSWORD=your_password
   DB_HOST=your-neon-db-hostname.neon.tech
   DB_PORT=5432
   DB_SSLMODE=require

   # Django Settings
   DEBUG=True
   SECRET_KEY=your-secret-key-here
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

8. Access the application:
   - Todo App: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin Interface: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Setting Up Neon PostgreSQL

1. Create a Neon account at [neon.tech](https://neon.tech)
2. Create a new project and database
3. Get connection details from the Neon dashboard
4. Update your `.env` file with these connection details

## Project Structure

```
django-todo-app/
│
├── todo_project/        # Project directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py      # Project settings
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py
│
├── todo_app/            # App directory
│   ├── migrations/      # Database migrations
│   ├── templates/       # HTML templates
│   ├── __init__.py
│   ├── admin.py         # Admin configuration
│   ├── apps.py
│   ├── forms.py         # Form definitions
│   ├── models.py        # Data models
│   ├── tests.py
│   ├── urls.py          # App URL configuration
│   └── views.py         # View definitions
│
├── static/              # Static files (CSS, JS, images)
├── .env                 # Environment variables (not in version control)
├── .gitignore           # Git ignore file
├── manage.py            # Django management script
└── requirements.txt     # Project dependencies
```

## Usage

- **Add a new task**: Click the "Add New Todo" button on the main page
- **View task details**: Click the "View" button on any task
- **Edit a task**: Click the "Edit" button on any task
- **Delete a task**: Click the "Delete" button on any task
- **Mark as complete/incomplete**: Click the corresponding button on any task

## Deployment

For production deployment:

1. Update your `.env` file with production settings:
   ```
   DEBUG=False
   ALLOWED_HOSTS=your-domain.com
   ```

2. Set up a production web server (like Nginx or Apache)
3. Configure a WSGI server (like Gunicorn)
4. Set up SSL for secure connections

## Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature/my-new-feature`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Django documentation
- Bootstrap team
- Neon PostgreSQL for database hosting
