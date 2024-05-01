from typing import Optional
from pydantic import BaseModel


class OrderTrackingBase(BaseModel):
    tracking_number: str
    order_id: int
    status: str


class OrderTrackingCreate(OrderTrackingBase):
    pass


class OrderTrackingUpdate(BaseModel):
    status: Optional[str] = None


class OrderTracking(OrderTrackingBase):
    id: int

    class Config:
        from_attributes = True
