from . import orders, order_details, order_tracking, recipes, menu_items, ingredients, customer, payments, promo_codes, reviews

from ..dependencies.database import engine, Base


def index():
    Base.metadata.create_all(engine)
