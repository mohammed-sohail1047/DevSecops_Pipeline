# Healthcare Microservices Project

## Services

### 1. Patient Service
Responsibilities:
- Patient registration
- Login API
- Profile management

APIs:
- POST /register
- POST /login
- GET /profile/{id}

---

### 2. Auth Service
- Patient registration
- Patient login

APIs:
- POST /auth/register
- POST /auth/login

---

### 3. Doctor Appointment Service
Responsibilities:
- List doctors
- Book appointment
- Cancel appointment
- Appointment history

APIs:
- GET /doctors
- POST /appointments
- DELETE /appointments/{id}
- GET /appointments/{patientId}

Sample Appointment Payload:
```json
{
  "patientId": "101",
  "doctorName": "Dr Sharma",
  "specialization": "Cardiology",
  "appointmentDate": "2026-06-01",
  "time": "11:30 AM"
}
```

---

### 4. Medical Report Service
Responsibilities:
- Upload patient reports
- Store reports in AWS S3
- Generate report download URL
- View uploaded reports

APIs:
- POST /upload-report
- GET /reports/{patientId}

Important:
- Uses AWS S3 for storage
- Uses `boto3` for AWS SDK integration
- Requires `S3_BUCKET_NAME`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_DEFAULT_REGION`

---

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- boto3

---

## Run Project

### Patient Service
uvicorn main:app --reload --port 8001

### Appointment Service
uvicorn main:app --reload --port 8000

### Report Service
uvicorn main:app --reload --port 8002