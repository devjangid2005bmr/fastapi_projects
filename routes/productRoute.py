from fastapi import APIRouter
from utils.utills import get_all_products

product_routes = APIRouter()

@product_routes.get("/")
def getAllProducts():
    return get_all_products()


@product_routes.post("/create")
def createNewProduct():
    return[]
 