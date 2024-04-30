from . import orders, order_details, recipes, sandwiches, resources, customer, payments, promo_codes, reviews

from ..dependencies.database import engine, Base


def index():
    Base.metadata.create_all(engine)
