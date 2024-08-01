from fastapi import FastAPI, Depends
from database import create_tables, delete_tables
from contextlib import asynccontextmanager
from models import Product
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
    product_id = await ProductsRepository.add_product(product)
    return {'product': product_id}


@app.post('/deleteProduct')
async def deleteProduct(id: int):
    await ProductsRepository.delete(id)
    return {'message': f'Удаление продукта {id}'}

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