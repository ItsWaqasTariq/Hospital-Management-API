from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Doctor
from schemas import DoctorCreate, DoctorResponse


router = APIRouter(
    prefix="/doctors",
    tags=["Doctors"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=DoctorResponse)
def create_doctor(
    doctor: DoctorCreate,
    db: Session = Depends(get_db)
):
    new_doctor = Doctor(
        name=doctor.name,
        specialization=doctor.specialization,
        phone=doctor.phone,
        email=doctor.email
    )

    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)

    return new_doctor

@router.get("/", response_model=list[DoctorResponse])
def get_doctors(db: Session = Depends(get_db)):
    doctors = db.query(Doctor).all()

    return doctors

@router.get("/{doctor_id}", response_model=DoctorResponse)
def get_doctor(
    doctor_id: int,
    db: Session = Depends(get_db)
):
    doctor = db.query(Doctor).filter(
        Doctor.id == doctor_id
    ).first()

    return doctor

@router.put("/{doctor_id}", response_model=DoctorResponse)
def update_doctor(
    doctor_id: int,
    doctor_data: DoctorCreate,
    db: Session = Depends(get_db)
):
    doctor = db.query(Doctor).filter(
        Doctor.id == doctor_id
    ).first()

    if doctor is None:
        return {"message": "Doctor not found"}

    doctor.name = doctor_data.name
    doctor.specialization = doctor_data.specialization
    doctor.phone = doctor_data.phone
    doctor.email = doctor_data.email

    db.commit()
    db.refresh(doctor)

    return doctor


@router.delete("/{doctor_id}")
def delete_doctor(
    doctor_id: int,
    db: Session = Depends(get_db)
):
    doctor = db.query(Doctor).filter(
        Doctor.id == doctor_id
    ).first()

    if doctor is None:
        return {"message": "Doctor not found"}

    db.delete(doctor)
    db.commit()

    return {"message": "Doctor deleted successfully"}

    