from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail


class OrderBase(BaseModel):
    # customer_name: str
    customer_name: Optional[str] = None
    customer_id: Optional[int] = None  # Allows null for guest orders
    description: Optional[str] = None
    is_guest: bool = True  # Indicates if the order is placed by a guest


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_id: Optional[int] = None
    description: Optional[str] = None
    is_guest: Optional[bool] = None  # Allow updating guest status if needed


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True
