# Django Ticketing System

Welcome to the Django Ticketing System project! This project is a web-based ticketing system developed using Django, a high-level Python web framework.

## Overview

The Django Ticketing System aims to provide a platform for managing tickets and user accounts. The project consists of several apps:

- **Tickets**: Handles the creation, management, and viewing of tickets.
- **Users**: Manages user accounts and authentication.

## Features

- **User Authentication**: Users can register, sign up, log in, and manage their accounts. Engineering users can be created from the admin panel.
- **Ticket Management**: Users can create, view, update, and close tickets.
- **Responsive Templates**: Utilizes Django templates for rendering dynamic and responsive web pages.
- **Database**: Default Django SQLite database is used for storing application data.


## Usage

1. **Download the Project**:
   - Download the project files either as a zip archive or in a folder.

2. **Setup Virtual Environment**:
   - Navigate to the project directory.
   - Create and activate the virtual environment:
     ```bash
     python -m venv .env
     source .env/bin/activate  # for Unix/Linux
     .env\Scripts\activate  # for Windows
     ```

3. **Install Dependencies**:
   - Install dependencies from `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

4. **Apply Migrations**:
   - Apply migrations to set up the database:
     ```bash
     python manage.py migrate
     ```

5. **Create Superuser**:
   - Create a superuser account for accessing the admin panel:
     ```bash
     python manage.py createsuperuser
     ```
   - Follow the prompts to enter a username, email, and password.

6. **Run the Server**:
   - Start the development server:
     ```bash
     python manage.py runserver
     ```
   - Access the application in your web browser at `http://localhost:8000`.

7. **Create Engineering Users**:
   - Log in to the Django admin panel using the superuser credentials at `http://localhost:8000/admin/`.
   - Navigate to the "Users" section and create engineering users as needed.

8. **Register Users And Create Ticket**:
    - Navigate to `http://localhost:8000/accounts/register-customer` to create a new customer
    - After loging in `http://localhost:8000/accounts/login` navigate to `http://localhost:8000/tickets/create-ticket` to submit a new ticket

9. **Accept a Ticket And Confirm Its Resolution**:
    - After an engineer account was registered by the admin panel login to the account
    - Navigate to `http://localhost:8000/tickets/ticket-queue` to see all ticket then accept or view more detail
    - To confirm the resolution of a ticket navigate to your workspace http://localhost:8000/tickets/workspace` and navigate to more detail from there you can confirm the resolution of the ticket
