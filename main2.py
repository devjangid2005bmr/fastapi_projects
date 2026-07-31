from fastapi import FastAPI
from routes.productRoute import product_routes
from routes.createpost import create_post


app = FastAPI(
    
    title = "api routes",
    description="hello how are you"
)

@app.get("/")
def home():
    return{
        "message":"heyyy baby"
    }
    
    
app.include_router(product_routes , prefix="/products")
app.include_router(create_post , prefix="/createpost")