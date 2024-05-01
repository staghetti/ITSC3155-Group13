from sqlalchemy.orm import Session
from datetime import date
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import func
from ..dependencies.database import get_db
from ..models import orders as model, menu_items as mi_model, order_details as od_model


def get_daily_revenue(db: Session, target_date: date):
    try:
        # Calculate the revenue based on orders for a specific day
        revenue = db.query(func.sum(mi_model.MenuItems.price * od_model.OrderDetail.amount)) \
                      .join(od_model.OrderDetail, od_model.OrderDetail.menu_item_id == mi_model.MenuItems.id) \
                      .join(model.Order, model.Order.id == od_model.OrderDetail.order_id) \
                      .filter(func.date(model.Order.order_date) == target_date) \
                      .scalar() or 0
        return revenue
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# Example usage in a FastAPI route
from fastapi import APIRouter, Depends

router = APIRouter(
    tags=['Revenue'],
    prefix="/revenue"
)


@router.get("/revenue/{target_date}", response_model=float)
def daily_revenue(target_date: date, db: Session = Depends(get_db)):
    revenue = get_daily_revenue(db, target_date)
    return revenue
