from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import order_details as controller
from ..schemas import order_details as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Order Details'],
    prefix="/orderdetails"
)


@router.post("/", response_model=schema.OrderDetail)
def create(request: schema.OrderDetailCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.OrderDetail])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{order_detail_id}", response_model=schema.OrderDetail)
def read_one(order_detail_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, order_detail_id=order_detail_id)


@router.put("/{order_detail_id}", response_model=schema.OrderDetail)
def update(order_detail_id: int, request: schema.OrderDetailUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, order_detail_id=order_detail_id)


@router.delete("/{order_detail_id}")
def delete(order_detail_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, order_detail_id=order_detail_id)
