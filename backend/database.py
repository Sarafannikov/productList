from sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

engine = create_async_engine("sqlite+aiosqlite:///productslists.db")

new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class ProductOrm(Model):
    __tablename__ = "Products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    quantity: Mapped[float]
    checked: Mapped[bool] = mapped_column(default=False)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
