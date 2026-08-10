from fastapi import FastAPI , status
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    message:str
    
    
    
@app.get("/user", response_model=User , status_code=status.HTTP_200_OK)
def get_user():
    return{
        "message":"fetched successfully",
        "name":"devv",
        "age":22,
        "password":"hello"
    }