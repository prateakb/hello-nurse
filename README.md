
# Nurse Scheduler Project

## Overview
Welcome to the Nurse Scheduler Django project! This README will guide you through setting up and running the project.

## Setting up the Project

1. **Install Python**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Django**: If Django is not installed, install it using pip:
    ```
    pip install django
    ```

3. **Clone the Repository**: Clone this repository to your local machine.

4. **Install Dependencies**: Navigate to the project directory and install any required dependencies:
    ```
    pip install -r requirements.txt
    ```

## Starting the App

1. **Navigate to Project Directory**: Open a terminal and navigate to the project's root directory.

2. **Run the Server**: Start the Django development server by running:
    ```
    python manage.py runserver
    ```

3. **Access the App**: Open your web browser and go to `http://localhost:8000` to view the app.

## Admin Password Setup

1. **Create Superuser**: To create an admin user, run:
    ```
    python manage.py createsuperuser
    ```
    Follow the prompts to set the username, email, and password.

2. **Access Admin Panel**: Once the server is running, access the admin panel at `http://localhost:8000/admin`. Log in with the superuser credentials.

## Database Migrations

1. **Initial Migration**: To set up your database, run:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

2. **Applying New Migrations**: Whenever you make changes to your database models, apply the migrations using the same commands.

## Additional Notes

- Familiarize yourself with the Django project structure and the MVC (Model-View-Controller) architecture.
- Regularly check the Django documentation for guidance: [Django Documentation](https://docs.djangoproject.com/en/stable/).

---
