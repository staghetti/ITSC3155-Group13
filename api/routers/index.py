from . import orders, order_details, payments, promo_codes, customers, ingredients


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(payments.router)
    app.include_router(promo_codes.router)
    app.include_router(customers.router)
    app.include_router(ingredients.router)
