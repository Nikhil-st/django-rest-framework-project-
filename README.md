Django REST Framework Project

A backend project built with Django REST Framework to learn and implement RESTful API development, serializers, CRUD operations, filtering, pagination, and database-driven API endpoints.

🚀 Features

* RESTful API development using Django REST Framework
* CRUD operations
* Model-based APIs
* Serializers for converting model instances to JSON
* API views and URL routing
* Pagination
* Filtering
* Multiple Django applications
* SQLite database integration
* Django migrations

🛠️ Tech Stack

Language:Python
Framework:Django
API Framework: Django REST Framework
Database:SQLite
Version Control: Git & GitHub

📂 Project Structure

```text
drf-project/
├── api/
│   ├── migrations/
│   ├── Serializers.py
│   ├── models.py
│   ├── pagination.py
│   ├── urls.py
│   └── views.py
│
├── blogs/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   └── views.py
│
├── employee/
│   ├── migrations/
│   ├── filters.py
│   ├── models.py
│   └── views.py
│
├── students/
│   ├── migrations/
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── django_rest_main/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt
```

⚙️ Installation & Setup

1. Clone the repository

```bash
git clone https://github.com/Nikhil-st/django-rest-framework-project-.git
cd django-rest-framework-project-
```

2. Create a virtual environment

```bash
python -m venv .venv
```

3. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```
 4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Apply migrations

```bash
python manage.py migrate
```

6. Run the development server

```bash
python manage.py runserver
```

The API can then be accessed through:

```text
http://127.0.0.1:8000/
```

📚 Key Learning Outcomes

Through this project, I practiced:

* REST API architecture
* Django REST Framework fundamentals
* Serializers
* API views
* CRUD operations
* URL routing
* Pagination
* Filtering
* Django models and migrations
* JSON-based API responses
* Git and GitHub workflow

🔮 Future Improvements

* Token/JWT authentication
* API documentation with Swagger/OpenAPI
* Unit and API tests
* Advanced filtering and searching
* Rate limiting
* PostgreSQL integration
* Cloud deployment

👨‍💻 Author

Nikhil Singh

B.Tech — Information Technology
Ajay Kumar Garg Engineering College
