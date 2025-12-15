# Tennis Club Web App

This is a simple web application built with Django that manages a tennis club's members. The app allows users to view a list of members, their details, and provides a testing page to display member data in a table format.

## Features

- View a list of members with their names.
- View detailed information about each member, including their phone number and join date.
- Testing page to display member data in a table format.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python (version 3.12 or higher)
- Django (version 5.1.3 or higher)

## Installation

1. Clone the repository:

2. Create a virtual environment (recommended):

   ```bash
   poetry venv .venv
   ```

3. Activate the virtual environment:

   ```bash
   # On Windows
   .venv\Scripts\activate


## Database

```psql
CREATE DATABASE tennis_club_db;
CREATE ROLE tennis_club_user WITH LOGIN PASSWORD 'Your_DB_password';
GRANT ALL PRIVILEGES ON DATABASE tennis_club_db TO tennis_club_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO tennis_club_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO tennis_club_user;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public TO tennis_club_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO tennis_club_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON SEQUENCES TO tennis_club_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON FUNCTIONS TO tennis_club_user;
```
