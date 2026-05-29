from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
import models, schemas
from database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Appointment Service")
sample_doctors = [
    {"id": 1, "name": "Dr Sharma", "specialization": "Cardiology"},
    {"id": 2, "name": "Dr Reddy", "specialization": "Neurology"},
    {"id": 3, "name": "Dr Gupta", "specialization": "Orthopedics"},
]
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
def root():
    return {"message": "Appointment Service Running"}
@app.get("/doctors", response_model=list[schemas.DoctorOut])
def list_doctors():
    return sample_doctors
@app.post("/appointments", response_model=schemas.AppointmentOut)
def create_appointment(appointment: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Appointment).filter(
        models.Appointment.doctor_name == appointment.doctorName,
        models.Appointment.appointment_date == appointment.appointmentDate,
        models.Appointment.time == appointment.time,
        models.Appointment.status == "booked",
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Slot already booked")
    db_appointment = models.Appointment(
        patient_id=appointment.patientId,
        doctor_name=appointment.doctorName,
        specialization=appointment.specialization,
        appointment_date=appointment.appointmentDate,
        time=appointment.time,
        status="booked",
        created_at=datetime.utcnow(),
    )
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment
@app.get("/appointments/{patient_id}", response_model=list[schemas.AppointmentOut])
def get_appointments(patient_id: str, db: Session = Depends(get_db)):
    appointments = db.query(models.Appointment).filter(models.Appointment.patient_id == patient_id).all()
    return appointments
@app.delete("/appointments/{appointment_id}")
def cancel_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = db.query(models.Appointment).filter(models.Appointment.id == appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    appointment.status = "cancelled"
    db.commit()
    return {"message": "Appointment cancelled", "appointment_id": appointment_id}
