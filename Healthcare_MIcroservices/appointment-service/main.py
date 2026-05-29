from fastapi import FastAPI

app = FastAPI()

appointments = []


@app.get("/")
def home():
    return {"message": "Appointment Service Running"}


@app.post("/appointments/book")
def book_appointment(doctor_id: int, appointment_time: str):

    # Double booking check
    for appointment in appointments:
        if (
            appointment["doctor_id"] == doctor_id
            and appointment["appointment_time"] == appointment_time
        ):
            return {"message": "Slot already booked"}

    new_appointment = {
        "doctor_id": doctor_id,
        "appointment_time": appointment_time,
        "status": "booked"
    }

    appointments.append(new_appointment)

    return {
        "message": "Appointment booked successfully",
        "appointment": new_appointment
    }


@app.get("/appointments/history")
def appointment_history():
    return {"appointments": appointments}


@app.put("/appointments/cancel/{id}")
def cancel_appointment(id: int):

    if id >= len(appointments):
        return {"message": "Appointment not found"}

    appointments[id]["status"] = "cancelled"

    return {
        "message": "Appointment cancelled",
        "appointment": appointments[id]
    }


@app.get("/doctors")
def list_doctors():

    doctors = [
        {
            "id": 1,
            "name": "Dr Sharma",
            "specialization": "Cardiology"
        },
        {
            "id": 2,
            "name": "Dr Reddy",
            "specialization": "Neurology"
        }
    ]

    return {"doctors": doctors}