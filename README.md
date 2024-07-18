# Django REST API Project

This is a Django REST API project connected to a Microsoft SQL Server (MSSQL) database. The project provides various endpoints to interact with the application's data.

## Table of Contents

-   [Installation](#installation)
-   [Configuration](#configuration)
-   [Running the Project](#running-the-project)
-   [API Endpoints](#api-endpoints)
-   [Authentication](#authentication)
-   [Testing](#testing)
-   [Deployment](#deployment)

## Installation

### Prerequisites

-   Python 3.9.13
-   Django 4.2.14
-   Microsoft SQL Server
-   `mssql-django` package

### Clone the Repository

```bash
git clone https://github.com/eolnuha/django-rest-api.git
cd django-rest-api
```

### Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

### Database Configuration

Ensure that you have an MSSQL database set up and that you have the connection details (host, port, username, password, and database name).

Update the DATABASES setting in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'your-database-name',
        'USER': 'your-username',
        'PASSWORD': 'your-password',
        'HOST': 'your-database-host',
        'PORT': 'your-database-port',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}
```

### Migrations

Apply the database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Running the project

Start the development server:

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`.

### Swagger Documentation

API documentation is available at `http://localhost:8000/swagger/`.
