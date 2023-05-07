from ninja import NinjaAPI

from products.api import router as products_router



api = NinjaAPI()


api.add_router("/products/", products_router, tags=['products'])
