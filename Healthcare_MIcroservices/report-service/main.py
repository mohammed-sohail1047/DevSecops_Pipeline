from fastapi import FastAPI, UploadFile, File
import os

app = FastAPI()

# Folder where reports will be stored
UPLOAD_FOLDER = "reports"

# Create folder if not exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {"message": "Report Service Running"}


# Upload Report API
@app.post("/reports/upload")
async def upload_report(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return {
        "message": "Report uploaded successfully",
        "filename": file.filename
    }


# List Reports API
@app.get("/reports/list")
def list_reports():

    files = os.listdir(UPLOAD_FOLDER)

    return {
        "reports": files
    }


# Download Report API
@app.get("/reports/download/{filename}")
def download_report(filename: str):

    file_path = os.path.join(UPLOAD_FOLDER, filename)

    if os.path.exists(file_path):
        return {
            "message": "Report found",
            "file_path": file_path
        }

    return {
        "message": "File not found"
    }