from fastapi import FastAPI
from routes.productRoute import product_routes


app = FastAPI(
    
    title = "api routes",
    description="hello how are you"
)

@app.get("/home")
def home():
    return{
        "message":"heyyy baby"
    }
    
    
app.include_router(product_routes , prefix="/products")
