from fastapi import FastAPI

app = FastAPI()

@app.get("/params")
def home():
    return {"message": "Welcome to the jungle"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"User ID": user_id}