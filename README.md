# Employee Management System 

A full-stack Django REST API for employee management, attendance, department structure, and performance. This project is containerized with Docker and deployed on **Render**, using **PostgreSQL** for the database and **DRF (Django REST Framework)** for API development.

---

##  Live Deployment

**Backend API:**  
🔗 [https://backend-intern-test.onrender.com](https://backend-intern-test.onrender.com)

---

##  Features

-  JWT-based Authentication (`/api/token/`)
-  CRUD operations for Employees & Departments
-  Attendance tracking (status: Present / Absent / Late)
-  Performance evaluations
-  Chart APIs for:
  - Monthly attendance overview
  - Employee distribution across departments
-  Admin panel (`/admin/`)
-  Swagger documentation (`/swagger/`)
-  Dockerized for production
-  PostgreSQL database integration

---

##  Project Structure
employee_project/

├── employees/ 

│ ├── models.py

│ ├── serializers.py

│ ├── views.py

│ ├── urls.py

│ └── management/commands/ # For seed_data.py

├── attendance/ 

│ ├── models.py

│ ├── serializers.py

│ ├── views.py

│ └── urls.py

├── performance/ 

│ ├── models.py

│ ├── serializers.py

│ ├── views.py

│ └── urls.py

├── employee_project/ 

│ ├── settings.py

│ ├── urls.py

│ └── wsgi.py

├── templates/ 

│ └── charts.html

├── requirements.txt

├── Dockerfile 

├── docker-compose.yml

├── .env.example

└── README.md

---

##  API Endpoints

### Authentication
- `POST /api/token/` — Get JWT token  
- `POST /api/token/refresh/` — Refresh token

###  Employees
- `GET /api/employees/employees/`
- `POST /api/employees/employees/`
- etc.

###  Departments
- `GET /api/employees/departments/`

###  Attendance
- `GET /api/attendance/attendance/`

###  Charts
- `GET /chart/employees-per-department/`
- `GET /chart/monthly-attendance/`

---

##  Seeding with Dummy Data & Migrations 

To apply migrations and seed data on Render (via one-time dev routes):

- [`/trigger-migrate/`](https://backend-intern-test.onrender.com/trigger-migrate/)
- [`/trigger-seed/`](https://backend-intern-test.onrender.com/trigger-seed/)

These endpoints apply migrations and populate fake data using `Faker`.

---

## Deployment with Docker

Docker is used for containerizing the app on Render.

### Local Setup:
```bash
git clone https://github.com/your-username/employee-management.git
cd employee-management
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


