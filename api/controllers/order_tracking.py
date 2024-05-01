from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import order_tracking as model
from sqlalchemy.exc import SQLAlchemyError


def create_tracking(db: Session, request):
    new_tracking = model.OrderTracking(
        tracking_number=request.tracking_number,
        order_id=request.order_id,
        status=request.status
    )

    try:
        db.add(new_tracking)
        db.commit()
        db.refresh(new_tracking)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_tracking


def read_all_tracking(db: Session):
    try:
        result = db.query(model.OrderTracking).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one_tracking(db: Session, tracking_id):
    try:
        tracking = db.query(model.OrderTracking).filter(model.OrderTracking.id == tracking_id).first()
        if not tracking:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order tracking not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return tracking


def update_tracking(db: Session, tracking_id, request):
    try:
        tracking = db.query(model.OrderTracking).filter(model.OrderTracking.id == tracking_id)
        if not tracking.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order tracking not found!")
        update_data = request.dict(exclude_unset=True)
        tracking.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return tracking.first()


def delete_tracking(db: Session, tracking_id):
    try:
        tracking = db.query(model.OrderTracking).filter(model.OrderTracking.id == tracking_id)
        if not tracking.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order tracking not found!")
        tracking.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
