# 🏥 Hospital Management API

A backend REST API for managing hospital operations such as **patients, doctors, departments, appointments, and medical records**.

This project is being developed as a learning project using **FastAPI, SQLAlchemy, and PostgreSQL**, with a focus on understanding backend architecture, database operations, API development, and programming logic.

## 🚀 Project Goals

The main goal of this project is to build a real-world backend while understanding how data travels through a FastAPI application:

```text
Client
   ↓
FastAPI Router
   ↓
Pydantic Schema
   ↓
SQLAlchemy Model
   ↓
Database Session
   ↓
PostgreSQL
   ↓
Response
   ↓
Client
```

Rather than building a large application all at once, the project is developed incrementally so each backend concept can be understood clearly.

## 🛠️ Technologies

* **Python**
* **FastAPI**
* **Pydantic**
* **SQLAlchemy**
* **PostgreSQL**
* **Uvicorn**
* **psycopg2**

## 📂 Project Structure

```text
hospital_api/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
│
└── routers/
    ├── patients.py
    └── doctors.py
```

### `main.py`

Creates the FastAPI application and registers API routers.

### `database.py`

Handles the PostgreSQL connection, SQLAlchemy engine, and database sessions.

### `models.py`

Contains SQLAlchemy models representing database tables such as `Patient` and `Doctor`.

### `schemas.py`

Contains Pydantic schemas used for request validation and response formatting.

### `routers/`

Contains API endpoints grouped by functionality.

For example:

* Patient CRUD
* Doctor CRUD

## 👨‍⚕️ Current Features

### Patient Management

* Create a patient
* Get all patients
* Get a patient by ID
* Update a patient
* Delete a patient

### Doctor Management

* Create a doctor
* Get all doctors
* Get a doctor by ID
* Update a doctor
* Delete a doctor

## 🔄 CRUD Operations

The API currently demonstrates the four fundamental database operations:

```text
CREATE → POST
READ   → GET
UPDATE → PUT
DELETE → DELETE
```

## 📚 Learning Roadmap

The project will continue to grow through the following stages:

```text
1. Project Structure
        ↓
2. PostgreSQL + SQLAlchemy
        ↓
3. Patient CRUD
        ↓
4. Doctor CRUD
        ↓
5. Department + Relationships
        ↓
6. Appointment Business Logic
        ↓
7. Medical Records
        ↓
8. JWT Authentication
        ↓
9. Transactions + Error Handling
        ↓
10. Sync → Async
        ↓
11. Connection Pooling
        ↓
12. PgBouncer + Production Architecture
```

## 🧠 Key Concepts

This project focuses on understanding concepts such as:

* REST APIs
* HTTP methods
* Request/response lifecycle
* Pydantic validation
* SQLAlchemy ORM
* Database sessions
* Transactions
* `commit()` and `refresh()`
* PostgreSQL
* CRUD operations
* Dependency injection
* API routing
* Database relationships
* Authentication
* Synchronous vs asynchronous programming
* Connection pooling
* Production backend architecture

## ▶️ Running the Project

Clone the repository:

```bash
git clone <your-repository-url>
cd hospital_api
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary
```

Configure your PostgreSQL database in `database.py`.

Then start the server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

## 🧪 API Testing

The API can be tested using FastAPI's built-in Swagger UI.

Example:

```text
POST /patients/
GET  /patients/
GET  /patients/{patient_id}
PUT  /patients/{patient_id}
DELETE /patients/{patient_id}
```

and:

```text
POST /doctors/
GET  /doctors/
GET  /doctors/{doctor_id}
PUT  /doctors/{doctor_id}
DELETE /doctors/{doctor_id}
```

## 🎯 Project Purpose

This project is designed to move beyond simply writing CRUD endpoints.

The focus is on understanding **why the code works**, how Python objects move through different components, and how a client request eventually becomes a database operation.

For example:

```text
JSON
 ↓
Pydantic Object
 ↓
SQLAlchemy Object
 ↓
Database Session
 ↓
PostgreSQL
 ↓
SQLAlchemy Object
 ↓
Response Schema
 ↓
JSON
```

## 📌 Project Status

🚧 **Currently in development**

Completed:

* Project structure
* FastAPI setup
* PostgreSQL connection
* SQLAlchemy setup
* Patient CRUD
* Doctor CRUD

Next:

* Department relationships
* Appointment business logic
* Medical records
* Authentication
* Advanced database and production concepts

---

**Built with Python, FastAPI, SQLAlchemy, and PostgreSQL.**
