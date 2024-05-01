from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import order_tracking as controller
from ..schemas import order_tracking as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Order Tracking'],
    prefix="/order_tracking"
)

@router.post("/", response_model=schema.OrderTracking)
def create_tracking(request: schema.OrderTrackingCreate, db: Session = Depends(get_db)):
    return controller.create_tracking(db=db, request=request)

@router.get("/", response_model=list[schema.OrderTracking])
def read_all_tracking(db: Session = Depends(get_db)):
    return controller.read_all_tracking(db)

@router.get("/{tracking_id}", response_model=schema.OrderTracking)
def read_one_tracking(tracking_id: int, db: Session = Depends(get_db)):
    return controller.read_one_tracking(db, tracking_id=tracking_id)

@router.put("/{tracking_id}", response_model=schema.OrderTracking)
def update_tracking(tracking_id: int, request: schema.OrderTrackingUpdate, db: Session = Depends(get_db)):
    return controller.update_tracking(db=db, request=request, tracking_id=tracking_id)

@router.delete("/{tracking_id}")
def delete_tracking(tracking_id: int, db: Session = Depends(get_db)):
    return controller.delete_tracking(db=db, tracking_id=tracking_id)
