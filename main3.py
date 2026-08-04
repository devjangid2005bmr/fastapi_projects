from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name:str
    age:int


app = FastAPI()

@app.post("/create_user")

def create_user(user:User):  #replace user:dict ---->> user:User .. for pydantic validation
    return{
        "message":"user successfully created",
        "data":user
    }