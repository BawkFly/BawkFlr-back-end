from fastapi import APIRouter

from routes.products.productsRoutes import productRoutes
from routes.user.userRoutes import userRoutes
from routes.offer.offerRoutes import offerRoutes

routes = APIRouter()

routes.include_router(userRoutes, prefix="/user", tags=["Usuario"])
routes.include_router(productRoutes, prefix="/product", tags=["Produto"])
routes.include_router(offerRoutes, prefix="/offer", tags=["Oferta"])
