from fastapi import FastAPI ,  HTTPException
import json

app = FastAPI()

def load_data():
    with open("data\patients.json",'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {"message": "Patient Management System"}

@app.get("/view")
def view():
    data = load_data()
    return data


@app.get("/patients/{patient_id}")
def view_patient(patient_id: int):
    data = load_data()
    
    for d in data:
        if d["patient_id"] == patient_id:
            return d
    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
