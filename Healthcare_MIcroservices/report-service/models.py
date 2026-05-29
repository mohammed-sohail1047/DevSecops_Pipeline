from sqlalchemy import Column, Integer, String, DateTime
from .database import Base


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String, nullable=False)
    filename = Column(String, nullable=False)
    s3_key = Column(String, nullable=False)
    s3_url = Column(String, nullable=False)
    uploaded_at = Column(DateTime, nullable=False)
