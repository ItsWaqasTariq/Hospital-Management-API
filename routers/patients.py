from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Patient
from schemas import PatientCreate, PatientResponse


router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=PatientResponse)
def create_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db)
):
    new_patient = Patient(
        name=patient.name,
        age=patient.age,
        gender=patient.gender,
        phone=patient.phone,
        address=patient.address
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return new_patient  

@router.get("/", response_model=list[PatientResponse])
def get_patients(db: Session = Depends(get_db)):
    patients = db.query(Patient).all()

    return patients    

@router.get("/{patient_id}", response_model=PatientResponse)
def get_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):
    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    return patient   


@router.delete("/{patient_id}")
def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):
    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if patient is None:
        return {"message": "Patient not found"}

    db.delete(patient)
    db.commit()

    return {"message": "Patient deleted successfully"}


@router.put("/{patient_id}", response_model=PatientResponse)
def update_patient(
    patient_id: int,
    patient_data: PatientCreate,
    db: Session = Depends(get_db)
):
    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if patient is None:
        return {"message": "Patient not found"}

    patient.name = patient_data.name
    patient.age = patient_data.age
    patient.gender = patient_data.gender
    patient.phone = patient_data.phone
    patient.address = patient_data.address

    db.commit()
    db.refresh(patient)

    return patient

