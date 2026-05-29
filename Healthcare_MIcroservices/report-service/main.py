from fastapi import FastAPI, HTTPException, UploadFile, File, Depends
from sqlalchemy.orm import Session
from datetime import datetime
import os
import uuid
import boto3
import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Report Service")

S3_BUCKET = os.getenv("S3_BUCKET_NAME")
AWS_REGION = os.getenv("AWS_DEFAULT_REGION", "us-east-1")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_s3_client():
    if not S3_BUCKET:
        raise HTTPException(status_code=500, detail="S3_BUCKET_NAME environment variable must be set")
    return boto3.client("s3", region_name=AWS_REGION)


@app.get("/")
def root():
    return {"message": "Report Service Running"}


# Upload Report API
@app.post("/upload-report", response_model=schemas.ReportOut)
async def upload_report(patientId: str, file: UploadFile = File(...), db: Session = Depends(get_db)):
    client = get_s3_client()
    file_extension = os.path.splitext(file.filename)[1]
    object_key = f"reports/{patientId}/{uuid.uuid4().hex}{file_extension}"
    file_content = await file.read()

    client.put_object(Bucket=S3_BUCKET, Key=object_key, Body=file_content, ContentType=file.content_type)

    s3_url = client.generate_presigned_url(
        ClientMethod="get_object",
        Params={"Bucket": S3_BUCKET, "Key": object_key},
        ExpiresIn=3600,
    )

    report = models.Report(
        patient_id=patientId,
        filename=file.filename,
        s3_key=object_key,
        s3_url=s3_url,
        uploaded_at=datetime.utcnow(),
    )
    db.add(report)
    db.commit()
    db.refresh(report)
    return report


@app.get("/reports/{patient_id}", response_model=list[schemas.ReportOut])
def get_reports(patient_id: str, db: Session = Depends(get_db)):
    reports = db.query(models.Report).filter(models.Report.patient_id == patient_id).all()
    return reports