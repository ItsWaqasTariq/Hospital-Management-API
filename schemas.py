from pydantic import BaseModel


class PatientCreate(BaseModel):
    name: str
    age: int
    gender: str
    phone: str
    address: str


class PatientResponse(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    phone: str
    address: str

    class Config:
        from_attributes = True

class DoctorCreate(BaseModel):
    name: str
    specialization: str
    phone: str
    email: str


class DoctorResponse(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    email: str

    class Config:
        from_attributes = True

