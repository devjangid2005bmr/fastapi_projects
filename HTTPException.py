from fastapi import FastAPI , status,HTTPException , Request
from fastapi.responses import JSONResponse

app = FastAPI()



@app.get("/user/{user_id}")
def get_user(user_id:int):
    if user_id !=1:
        raise HTTPException(
            status_code=404,
            detail= "user not found" 
        )
    return{
        "id":1,
        "name":"dev"
    }
    
    




class user_not_found(Exception):
    def __init__(self, name:str):
        self.name = name
        
@app.exception_handler(user_not_found)  
def user_not_found_function(request:Request , exc:user_not_found): 
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "message":f"{exc.name}     nahi mila "
        }
    )

@app.get("/username/{name}")
def user(name:str):
    if name != "devv":
        raise user_not_found(name)
    return{
        "name":f"{name}   mil gaya"
    }
