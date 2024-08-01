import sqlalchemy
from sqlalchemy import select, delete

from database import new_session, ProductOrm
from models import Product

class ProductsRepository:
    @classmethod
    async def add_product(cls, data: Product) -> int:
        async with new_session() as session:
            product_dict = data.model_dump()

            product = ProductOrm(**product_dict)
            session.add(product)
            await session.flush()
            await session.commit()
            return product.id

    @classmethod
    async def get_all(cls):
        async with new_session() as session:
            query = select(ProductOrm)
            result = await session.execute(query)
            product_models = result.scalars().all()
            return product_models

    @classmethod
    async def delete(cls, id):
        async with new_session() as session:
            query = delete(ProductOrm).where(ProductOrm.id == id)
            result = await session.execute(query)
            await session.commit()
            return True

    @classmethod
    async def delete_all(cls):
        async with new_session() as session:
            query = delete(ProductOrm)
            result = await session.execute(query)
            await session.commit()
            return True
