from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Product
from web_project_microshop.api_v1.products.schemas import (
    ProductCreate,
    ProductUpdate,
    ProductUpdatePartial,
)


async def get_products(session: AsyncSession) -> list[Product]:
    stmt = select(Product).order_by(Product.id)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)


async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)


async def create_product(
    session: AsyncSession, product_in: ProductCreate
) -> Product | None:
    Product(**product_in.model_dump())
    session.add(product)  # type: ignore
    await session.commit()
    await session.refresh(product)  # type: ignore
    return product  # type: ignore


async def update_product(
    session: AsyncSession,
    product: Product,
    product_update: ProductUpdate | ProductUpdatePartial,
    partial: bool = False,
) -> Product:
    for name, value in product_update.model_dump().items():
        setattr(product, name, value)
    await session.commit()
    return product


async def update_product_partial(
    session: AsyncSession,
    product: Product,
    product_update_partial: ProductUpdatePartial,
):
    for name, value in product_update.model_dump(exclude_unset=True).items():  # type: ignore
        setattr(product, name, value)
    await session.commit()
    return product


async def delete_product(
    session: AsyncSession,
    product: Product,
) -> None:
    await session.delete(product)
