from fastapi import FastAPI, Depends
from database import create_tables, delete_tables
from contextlib import asynccontextmanager
from models import Product, testId
from typing import Annotated
from repository import ProductsRepository
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await delete_tables()
    await create_tables()
    print("Перезапуск")
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/getProducts")
async def getProducts():
    products = await ProductsRepository.get_all()
    return products


@app.post("/addProduct")
async def addProduct(product: Product):
    products = await ProductsRepository.get_all()
    print(len(products))
    if len(products) > 15:
        return {'error': 'Максимум 15 элементов'}
    product_id = await ProductsRepository.add_product(product)
    return {'product': product_id}


@app.post('/deleteProduct')
async def deleteProduct(product_id: testId):
    await ProductsRepository.delete(product_id.product_id)
    return {'message': f'Удаление продукта {product_id.product_id}'}

@app.post('/deleteAll')
async def deleteAll():
    await ProductsRepository.delete_all()
    return {'message': 'Список продуктов стерт'}

origins = [
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)