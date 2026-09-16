# 🏥 Hospital Management API

A backend REST API built with **FastAPI, SQLAlchemy, and PostgreSQL** for managing hospital patients and doctors.

## 🛠️ Technologies

* Python
* FastAPI
* Pydantic
* SQLAlchemy
* PostgreSQL
* Uvicorn
* psycopg2

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

## 👨‍⚕️ Patient Management

The API currently supports CRUD operations for patients.

### Patient Fields

* ID
* Name
* Age
* Gender
* Phone
* Address

### Patient Endpoints

```text
POST   /patients/
GET    /patients/
GET    /patients/{patient_id}
PUT    /patients/{patient_id}
DELETE /patients/{patient_id}
```

## 👨‍⚕️ Doctor Management

The API also supports CRUD operations for doctors.

### Doctor Fields

* ID
* Name
* Specialization
* Phone
* Email

### Doctor Endpoints

```text
POST   /doctors/
GET    /doctors/
GET    /doctors/{doctor_id}
PUT    /doctors/{doctor_id}
DELETE /doctors/{doctor_id}
```

## 🗄️ Database

The project uses **PostgreSQL** as the database and **SQLAlchemy ORM** for database operations.

Current database tables:

```text
PostgreSQL
   │
   ├── patients
   │
   └── doctors
```

## 🔄 Request Flow

The API follows this basic flow:

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

For example, when creating a patient:

```text
JSON
 ↓
PatientCreate
 ↓
patient
 ↓
Patient
 ↓
new_patient
 ↓
db.add()
 ↓
db.commit()
 ↓
PostgreSQL
 ↓
db.refresh()
 ↓
Response
```

## 🧪 API Documentation

FastAPI provides interactive Swagger UI for testing the endpoints:

```text
http://127.0.0.1:8000/docs
```

## 📌 Current Status

The current version includes:

* FastAPI project setup
* PostgreSQL database connection
* SQLAlchemy configuration
* Patient CRUD
* Doctor CRUD
* Pydantic request/response schemas
* API testing through Swagger UI

**Project is currently under development.**
