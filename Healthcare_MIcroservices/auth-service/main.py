from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Auth Service Running"}


@app.post("/auth/register")
def register():
    return {"message": "User registered"}


@app.post("/auth/login")
def login():
    return {"token": "jwt-token"}