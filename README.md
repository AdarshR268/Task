# Recruit Dashboard

A Django-based web application for managing student recruitment. This project allows an admin user to securely log in, add new students, view a list of all students, and search/filter students by their course interest.

## Features

- **Admin Authentication**: Secure login and logout functionality for admin users.
- **Student Management**: Add new students with fields for Name, Email, Course Interest, and Status (New, Contacted, Enrolled).
- **Duplicate Prevention**: Automatically checks and alerts if a student's email already exists in the database.
- **Search & Filter**: Search functionality on the student list page to filter students by their course interest.
- **Responsive UI**: Clean, modern interface built with standard Bootstrap 4.

## AI Assistant Used
This project was rapidly developed with the assistance of an AI coding agent:
**Name:** Antigravity

### Prompts Used During Development
Below is the list of prompts provided to Antigravity to build out this project step-by-step:

1. *"Create a Django model Student with fields: name (CharField), email (EmailField), course_interest (CharField), status (CharField with choices like New, Contacted, Enrolled)"*
2. *"Create a home.html form for adding a new Student with all fields in templates"*
3. *"add path urls.py and Create views to add a student and list all students."*
4. *"Add search/filter functionality in the list view based on course_interest,make changes in html and views accordingly"*
5. *"check whether the email id is already in db ,if it is duplicate show a message to front end..change accodingly to views and html pages"*
6. *"create a login page for login admin user and ,redirect to add student page after successfull login,make changes in views and urls accordingly"*
7. *"also create a logout button in home.html and list.hml and add in urls and create views for logout also afterlogout,redirect to login page"*

## Setup Instructions

1. Clone the repository.
2. Install the required dependencies (`pip install django`).
3. Run migrations to set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Create an admin superuser to log in:
   ```bash
   python manage.py createsuperuser
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```
6. Visit `http://127.0.0.1:8000/` to access the application.
