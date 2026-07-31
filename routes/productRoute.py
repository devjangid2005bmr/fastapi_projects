from fastapi import APIRouter, HTTPException , Path
from utils.utills import get_all_products

product_routes = APIRouter()

@product_routes.get("/productid/{id}")
def get_product(id: int):
    

    products = get_all_products()
    

    for product in products:
        if product["id"] == id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
    
@product_routes.get("/productname/{name}")
def get_name(name: str):
    names = get_all_products()

    for n in names:
        if n["name"] == name:
            return n

    raise HTTPException(
        status_code=404,
        detail="ERROR 404"
    )