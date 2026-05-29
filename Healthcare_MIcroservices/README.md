# Healthcare Microservices Project

## Services

### 1. Auth Service
- Patient registration
- Patient login

### APIs
- POST /auth/register
- POST /auth/login

---

### 2. Appointment Service
- Book appointment
- View appointment history
- Cancel appointment
- Prevent double booking

### APIs
- POST /appointments/book
- GET /appointments/history
- PUT /appointments/cancel/{id}

---

### 3. Report Service
- Upload medical reports
- List reports
- Download reports

### APIs
- POST /reports/upload
- GET /reports/list
- GET /reports/download/{filename}

---

## Tech Stack
- Python
- FastAPI
- REST APIs

---

## Run Project

### Appointment Service
uvicorn main:app --reload --port 8000

### Auth Service
uvicorn main:app --reload --port 8001


### Report Service
uvicorn main:app --reload --port 8002