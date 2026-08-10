from fastapi import FastAPI , Depends , HTTPException , status , Request
from utils.utills import get_all_products
from fastapi.responses import JSONResponse


app = FastAPI()


class ProductNotFound(Exception):
    def __init__(self, id):
        self.id = id

@app.exception_handler(ProductNotFound)
def product_not_found(request:Request , exc:ProductNotFound):
    return JSONResponse(
        status_code=404,
        content={
            "status":"not found",
            "message":f"{exc.id} :  not found"
        }
    )
    


def get_products():
    return get_all_products()

@app.get("/products{id}")
def products(
    id: int,
    products = Depends(get_products)
):
    for product in products:
        if product["id"]==id:
            return product
        
    raise ProductNotFound(id)
    
        
    