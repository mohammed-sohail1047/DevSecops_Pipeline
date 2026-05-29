from sqlalchemy import Column, Integer, String, DateTime
from .database import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String, nullable=False)
    doctor_name = Column(String, nullable=False)
    specialization = Column(String, nullable=False)
    appointment_date = Column(String, nullable=False)
    time = Column(String, nullable=False)
    status = Column(String, nullable=False, default="booked")
    created_at = Column(DateTime, nullable=False)
