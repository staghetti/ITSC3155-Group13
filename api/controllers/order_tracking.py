from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import order_tracking as model
from sqlalchemy.exc import SQLAlchemyError

def track_order(tracking_number: str, db: Session):
    try:
        order = db.query(model.OrderTracking).filter(model.OrderTracking.tracking_number == tracking_number).first()
        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found!")
        return order
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
