# VPS Manager

## Overview

`VPS Manager` is a Django-based web application designed to manage virtual private servers (VPS) through a RESTful API. Built with Django 5.1.4 and Django REST Framework, it allows users to store, retrieve, update, and delete VPS information, including unique identifiers, CPU, RAM, HDD, and server status. The project is in its early stages, focusing on API functionality with plans for future enhancements like a web interface and admin panel integration.

### Features
- **VPS Management**: Store and manage VPS details (UID, CPU, RAM, HDD, status) in a SQLite database.
- **REST API**: Perform CRUD operations on VPS data via endpoints like `/api/vps/` and `/api/vps/<id>/`.
- **Status Updates**: Change VPS status (started, blocked, stopped) using a custom API endpoint (`/api/vps/<id>/change_status/`).
- **Filtering and Sorting**: Filter VPS by status, CPU, RAM, or HDD, and sort by CPU, RAM, or HDD.
- **Admin Panel**: Accessible at `/admin/`, but VPS model integration is pending.

## Project Status
The project is in early development:
- Fully functional REST API for VPS management.
- No frontend templates or admin panel configuration for the VPS model yet.
- Tests are not implemented.
Future plans include adding a web interface, admin panel support, and tests.

## Installation

### Prerequisites
- Python 3.8+
- Django 5.1.4
- Django REST Framework
- SQLite (included with Python)

### Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Glazzz123/vps_manager.git
   cd vps_manager
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install django==5.1.4 djangorestframework
   ```

4. **Apply migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   - **API**: `http://127.0.0.1:8000/api/vps/`
   - **Admin Panel**: `http://127.0.0.1:8000/admin/`

## Usage
- **API Endpoints**:
  - `GET /api/vps/`: List all VPS or create a new VPS.
  - `GET /api/vps/<id>/`: Retrieve a specific VPS.
  - `PUT/PATCH /api/vps/<id>/`: Update a VPS.
  - `DELETE /api/vps/<id>/`: Delete a VPS.
  - `PATCH /api/vps/<id>/change_status/`: Change the status of a VPS (e.g., `{"status": "started"}`).
  - Supports query parameters for filtering (e.g., `?search=started`) and sorting (e.g., `?ordering=cpu`).
- **Admin Panel**:
  - Log in at `/admin/` to manage Django models (VPS model not yet registered).
- **Frontend**:
  - No frontend templates are implemented yet. Future updates may include a web interface for VPS management.

## Project Structure
```
vps_manager/
├── manage.py           # Django command-line utility
├── db.sqlite3         # SQLite database (not included in repo)
├── vps_manager/       # Project configuration
│   ├── __init__.py
│   ├── settings.py    # Django settings
│   ├── asgi.py        # ASGI configuration
│   ├── wsgi.py        # WSGI configuration
│   ├── urls.py        # Main URL routing
├── vps/               # VPS management application
│   ├── __init__.py
│   ├── apps.py        # Application configuration
│   ├── admin.py       # Admin panel configuration (empty)
│   ├── models.py      # VPS model
│   ├── serializers.py # API serializers
│   ├── views.py       # API views
│   ├── urls.py        # API URL routing
│   ├── tests.py       # Tests (empty)
│   ├── migrations/
│   │   ├── 0001_initial.py  # Initial migration for VPS model
│   │   ├── __init__.py
└── templates/         # Directory for templates (not yet implemented)
```

## Models
- **VPS**:
  - `uid`: Unique identifier (string, max 100 characters).
  - `cpu`: Number of CPU cores (integer).
  - `ram`: RAM in MB (integer).
  - `hdd`: Disk space in GB (integer).
  - `status`: Server status (`started`, `blocked`, `stopped`).

## API Examples
- **List all VPS**:
  ```bash
  curl http://127.0.0.1:8000/api/vps/
  ```
- **Filter by status**:
  ```bash
  curl http://127.0.0.1:8000/api/vps/?search=started
  ```
- **Change VPS status**:
  ```bash
  curl -X PATCH -H "Content-Type: application/json" -d '{"status": "started"}' http://127.0.0.1:8000/api/vps/1/change_status/
  ```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or suggestions, contact the repository owner via GitHub issues.