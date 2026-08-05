from fastapi import APIRouter, HTTPException, Path
from utils.utills import get_all_products

product_routes = APIRouter()


@product_routes.get("/productid/{id}")
def get_product(
    id: int = Path(..., gt=0, description="Product ID")):
    
    products = get_all_products()

    for product in products:
        if product["id"] == id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )


@product_routes.get("/productname/{name}")
def get_product_by_path(name: str):
    products = get_all_products()

    for product in products:
        if product["name"].lower() == name.lower():
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )


@product_routes.get("/productname")
def get_product_by_query(name: str):
    products = get_all_products()

    for product in products:
        if product["name"].lower() == name.lower():
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )