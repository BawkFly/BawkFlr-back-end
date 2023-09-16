import datetime as datetime

from app.repositories.products.productRepository import ProductRepository
from fastapi import HTTPException, status
from sqlalchemy.orm import Session


class GetProductByIdService:
    def __init__(self, db=Session) -> None:
        self.product_repository = ProductRepository(db)

    def execute(self, id: str):
        show_product = self.product_repository.find_by_id(id)
        if not show_product:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Este produto não existe.")

        return show_product
        return show_product
