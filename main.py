from fastapi import FastAPI

from database import engine, Base
from models import Patient
from routers.patients import router as patient_router
from routers.doctors import router as doctor_router


app = FastAPI(title="Hospital Management API")


Base.metadata.create_all(bind=engine)


app.include_router(patient_router)
app.include_router(doctor_router)

