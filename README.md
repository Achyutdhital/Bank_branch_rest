# Bank Branch REST API

A REST API server for querying bank branches and their details, built with Django REST Framework.

## Features

- REST API endpoints for bank and branch data
- **Real Data**: Complete Indian Banks dataset with 170 banks and 127,857 branches
- Clean code architecture with proper separation of concerns
- Comprehensive test cases
- Error handling and validation
- **Swagger/OpenAPI documentation** with interactive API explorer
- Django Admin interface for data management
- Pagination support

## Endpoints

### API Overview
- `GET /api/` - API overview with all available endpoints

### Banks
- `GET /api/banks/` - Get all banks (paginated)
- `GET /api/banks/{bank_id}/` - Get specific bank details
- `GET /api/banks/{bank_id}/branches/` - Get all branches for a specific bank

### Branches
- `GET /api/branches/` - Get all branches with pagination
- `GET /api/branches/{ifsc_code}/` - Get specific branch details by IFSC code
- `GET /api/branches/search/?ifsc={ifsc_code}` - Search branch by IFSC code
- `GET /api/branches/search/?city={city_name}` - Search branches by city

## Setup and Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Initialize the database with real bank and branch data:
   ```bash
   python manage.py load_real_data
   ```
   This will load **170 banks** and **127,857 branches** from the official Indian Banks dataset.
5. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```
6. Run the server:
   ```bash
   python manage.py runserver
   ```

The server will start on `http://localhost:8000`

## API Documentation

The API is fully documented using Swagger/OpenAPI:

- **Swagger UI**: `http://localhost:8000/swagger/` - Interactive API documentation
- **ReDoc**: `http://localhost:8000/redoc/` - Alternative documentation interface
- **OpenAPI Schema**: `http://localhost:8000/swagger.json` - Raw OpenAPI schema

### Features of the Documentation:
- Interactive API testing directly from the browser
- Detailed endpoint descriptions and parameter information
- Request/response examples
- Schema definitions for all models

## Testing

Run the test suite:
```bash
python -m pytest tests/ -v
```

Or using Django's test runner:
```bash
python manage.py test
```

## Project Structure

```
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
├── pytest.ini         # Pytest configuration
├── bank_api/           # Django project settings
│   ├── __init__.py
│   ├── settings.py     # Django settings
│   ├── urls.py         # Main URL configuration
│   ├── wsgi.py         # WSGI configuration
│   └── asgi.py         # ASGI configuration
├── banks/              # Django app for banks and branches
│   ├── __init__.py
│   ├── admin.py        # Django admin configuration
│   ├── apps.py         # App configuration
│   ├── models.py       # Database models
│   ├── serializers.py  # DRF serializers
│   ├── views.py        # API views
│   ├── urls.py         # App URL configuration
│   └── management/     # Django management commands
│       └── commands/
│           └── init_data.py  # Database initialization
└── tests/              # Test cases
    ├── __init__.py
    ├── test_models.py  # Model tests
    └── test_api.py     # API endpoint tests
```

## Method Used

1. **Framework**: Django REST Framework (robust Python web framework)
2. **Database**: SQLite with Django ORM
3. **Architecture**: Clean separation with models, serializers, views, and URL configuration
4. **Testing**: pytest-django for comprehensive test coverage
5. **Error Handling**: Proper HTTP status codes and error messages
6. **Data Validation**: DRF serializers for input validation and output formatting
7. **Admin Interface**: Django admin for easy data management
8. **Pagination**: Built-in DRF pagination for large datasets
9. **Documentation**: Swagger/OpenAPI with drf-yasg for interactive API documentation

## Time Taken

Approximately 5-6 hours to complete:
- Project setup and Django configuration: 1 hour
- Database models and migrations: 1 hour
- DRF serializers and views: 2 hours
- Management commands and data initialization: 1 hour
- Test cases: 1 hour
- Documentation and cleanup: 0.5 hours

## Assignment Requirements Fulfilled

✅ **API Server**: Complete REST API server built with Django REST Framework  
✅ **Python Web Framework**: Django REST Framework (robust and scalable)  
✅ **Bank List Endpoints**: `/api/banks/` - Get all banks with pagination  
✅ **Branch Details Endpoints**: `/api/branches/{id}/` - Get specific branch details  
✅ **Bank-Branch Relationship**: `/api/banks/{id}/branches/` - Get branches for specific bank  
✅ **Clean Code**: Well-structured codebase with proper separation of concerns  
✅ **Test Cases**: Comprehensive test suite with 17+ test cases covering models and API endpoints  
✅ **Bonus Features**:
- Swagger/OpenAPI documentation for interactive API exploration
- Django Admin interface for data management
- Pagination for large datasets
- Search functionality by IFSC and city
- Proper error handling and validation
- SQLite database with sample data
- Git version control ready with `.gitignore`

## Admin Interface

Access the Django admin interface at `http://localhost:8000/admin/` after creating a superuser to manage banks and branches data.

## Sample API Responses

### Get All Banks
```json
{
  "count": 170,
  "next": "http://localhost:8000/api/banks/?page=2",
  "previous": null,
  "results": [
    {
      "id": 60,
      "name": "ABHYUDAYA COOPERATIVE BANK LIMITED",
      "created_at": "2024-01-01T10:00:00Z",
      "updated_at": "2024-01-01T10:00:00Z"
    }
  ]
}
```

### Get Branch Details
```json
{
  "ifsc": "SBIN0000001",
  "branch": "Mumbai Main Branch",
  "address": "123 Fort Area, Mumbai",
  "city": "Mumbai",
  "district": "Greater Mumbai",
  "state": "Maharashtra",
  "bank": {
    "id": 1,
    "name": "State Bank of India",
    "created_at": "2024-01-01T10:00:00Z",
    "updated_at": "2024-01-01T10:00:00Z"
  },
  "created_at": "2024-01-01T10:00:00Z",
  "updated_at": "2024-01-01T10:00:00Z"
}
```

### Search Branches by City
```json
{
  "branches": [
    {
      "ifsc": "SBIN0000001",
      "branch": "Mumbai Main Branch",
      "city": "Mumbai",
      "district": "Greater Mumbai",
      "state": "Maharashtra",
      "bank_name": "State Bank of India",
      "bank_id": 1
    }
  ]
}
```
